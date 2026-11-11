"""
Checking a webhook AfroPin sent you. Each one carries three headers: webhook-id (the same on every retry of one event),
webhook-timestamp (Unix seconds, when it was sent) and webhook-signature, the HMAC-SHA256 of "id.timestamp.body" with
your webhook's secret. Check it against the body exactly as received (request.get_data() in Flask, request.body in
Django), before parsing it. A timestamp more than 5 minutes from now is refused, so a captured webhook can't be
replayed later.

    event = webhooks.parse(request.get_data(), request.headers, WEBHOOK_SECRET)
"""

import hashlib
import hmac
import json
import time

from .errors import AfroPinError

TOLERANCE = 300


def verify(raw_body, headers, secret, tolerance=TOLERANCE):
    try:
        _check(raw_body, headers, secret, tolerance)
        return True
    except AfroPinError:
        return False


def parse(raw_body, headers, secret, tolerance=TOLERANCE):
    """
    The event, {"id": ..., "type": "pin.sold", "data": {...}}, once its signature checks out. Use id to skip an event
    you've already handled.
    """
    event_id = _check(raw_body, headers, secret, tolerance)
    event = json.loads(raw_body)
    if not isinstance(event, dict) or "type" not in event:
        raise AfroPinError("invalid_response", "The webhook body is not an AfroPin event")
    return {"id": event_id, **event}


def _check(raw_body, headers, secret, tolerance):
    # Any mapping of headers (Flask and Django's request.headers, or a dict), matched without regard to case
    found = {str(k).lower().replace("_", "-"): str(v).strip() for k, v in (headers or {}).items()}
    event_id = found.get("webhook-id", "")
    timestamp = found.get("webhook-timestamp", "")
    signature = found.get("webhook-signature", "")
    if not event_id or not timestamp.isdigit() or not signature:
        raise AfroPinError("invalid_signature", "The webhook-id, webhook-timestamp or webhook-signature header is missing")
    if abs(int(time.time()) - int(timestamp)) > tolerance:
        raise AfroPinError("invalid_signature", "The webhook timestamp is too old or too far ahead: check your server clock")
    body = raw_body if isinstance(raw_body, bytes) else raw_body.encode()
    expected = hmac.new(secret.encode(), ("%s.%s." % (event_id, timestamp)).encode() + body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise AfroPinError("invalid_signature", "The webhook signature does not match its body")
    return event_id
