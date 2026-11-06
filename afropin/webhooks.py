"""
Checking a webhook AfroPin sent you. Each one is signed with the webhook's secret: the webhook-secret header holds the
HMAC-SHA256 of the raw body. Check it against the body exactly as received (request.get_data() in Flask, request.body in
Django), before parsing it.
"""

import hashlib
import hmac
import json

from .errors import AfroPinError


def verify(raw_body, signature, secret):
    if not signature:
        return False
    body = raw_body if isinstance(raw_body, bytes) else raw_body.encode()
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


def parse(raw_body, signature, secret):
    """The event, {"type": "pin.sold", "data": {...}}, once its signature checks out."""
    if not verify(raw_body, signature, secret):
        raise AfroPinError("invalid_signature", "The webhook signature does not match its body")
    event = json.loads(raw_body)
    if not isinstance(event, dict) or "type" not in event:
        raise AfroPinError("invalid_response", "The webhook body is not an AfroPin event")
    return event
