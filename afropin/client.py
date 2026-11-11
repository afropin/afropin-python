"""The AfroPin API client: request signing, idempotency keys, responses and errors."""

import hashlib
import hmac
import json
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request

from .errors import AfroPinError
from .page import Page

VERSION = "2.1.0"
BASE_URL = "https://afropin.com/api/v1"


class Client:
    """
    Signs every request with your key (HMAC-SHA256 over "METHOD.path.timestamp.nonce.sha256(body)"), sends a fresh
    Idempotency-Key with each one, and returns the response's data. Your key's mode (test or live) decides which records
    you work with.

        afropin = Client("key_id", "secret")
        pin = afropin.reseller.pins.sell({"catalog_id": "...", "amount": 5000, ...})

    Requests are never retried for you: a retried sale with the same external_reference fails safely with
    duplicate_external_reference, so retry yourself with a new idempotency key when you need to.
    """

    def __init__(self, key_id, secret, base_url=BASE_URL, timeout=30, transport=None):
        from .resources import Brand, Reseller

        self._key_id = key_id
        self._secret = secret
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        # transport(method, url, headers, body) -> (status, raw body): for tests
        self._transport = transport
        self.reseller = Reseller(self)
        self.brand = Brand(self)

    def request(self, method, path, params=None, idempotency_key=None, list_=False):
        """Send one request: its data, or a Page for lists. params are the query (GET, DELETE) or the JSON body."""
        params = params or {}
        url = "%s/%s" % (self._base_url, path.lstrip("/"))
        body = ""
        if method in ("GET", "DELETE"):
            query = {key: value for key, value in params.items() if value is not None}
            if query:
                url += "?" + urllib.parse.urlencode(query)
        else:
            body = json.dumps(params, separators=(",", ":"), ensure_ascii=False)

        timestamp = str(int(time.time()))
        nonce = str(uuid.uuid4())
        signed_path = urllib.parse.urlparse(url).path.lstrip("/")
        canonical = ".".join([method, signed_path, timestamp, nonce, hashlib.sha256(body.encode()).hexdigest()])
        headers = {
            "X-Key-Id": self._key_id,
            "X-Timestamp": timestamp,
            "X-Nonce": nonce,
            "X-Signature": hmac.new(self._secret.encode(), canonical.encode(), hashlib.sha256).hexdigest(),
            "Idempotency-Key": idempotency_key or str(uuid.uuid4()),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "afropin-python/%s" % VERSION,
        }

        status, raw = (self._transport or self._send)(method, url, headers, body)
        try:
            payload = json.loads(raw)
        except ValueError:
            raise AfroPinError("invalid_response", "The API sent a response that is not JSON", status=status)
        if not payload.get("ok"):
            error = payload.get("error") or {}
            raise AfroPinError(error.get("code", "unknown_error"), error.get("message", "The request failed"), error.get("fields"), status)

        return Page(payload.get("data") or [], payload.get("paging")) if list_ else payload.get("data")

    def _send(self, method, url, headers, body):
        request = urllib.request.Request(url, data=body.encode() if body else None, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=self._timeout) as response:
                return response.status, response.read().decode()
        except urllib.error.HTTPError as error:
            return error.code, error.read().decode()
        except (urllib.error.URLError, OSError) as error:
            raise AfroPinError("connection_failed", "Could not reach the AfroPin API: %s" % error)
