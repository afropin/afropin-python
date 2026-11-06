"""
The Python SDK's checks: signing and webhooks offline, then (with AFROPIN_TEST_ENV pointing at a JSON file of test keys,
base_url, catalog_id and test_pin) a real round trip against an AfroPin API in test mode.
    python3 -m unittest discover -s tests
"""

import hashlib
import hmac
import json
import os
import secrets
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from afropin import AfroPinError, Client, Page, webhooks  # noqa: E402


class Offline(unittest.TestCase):
    def test_signs_requests_and_returns_data(self):
        sent = {}

        def transport(method, url, headers, body):
            sent.update(method=method, url=url, headers=headers, body=body)
            return 200, '{"ok":true,"data":{"pin_id":"p1"}}'

        client = Client("key_1", "secret_1", base_url="https://example.test/api/v1", transport=transport)
        data = client.reseller.pins.top_up({"pin_id": "p1", "amount": 500}, idempotency_key="idem-1")
        h = sent["headers"]
        canonical = ".".join(["POST", "api/v1/reseller/pins/top-up", h["X-Timestamp"], h["X-Nonce"], hashlib.sha256(sent["body"].encode()).hexdigest()])
        self.assertEqual(h["X-Signature"], hmac.new(b"secret_1", canonical.encode(), hashlib.sha256).hexdigest())
        self.assertEqual(h["Idempotency-Key"], "idem-1")
        self.assertEqual(data, {"pin_id": "p1"})
        client.reseller.pins.get("a/b")
        self.assertTrue(sent["url"].endswith("/reseller/pins/a%2Fb"))
        self.assertEqual(sent["body"], "")

    def test_verifies_webhooks(self):
        body = '{"type":"pin.sold","data":{"pin_id":"p1"}}'
        self.assertTrue(webhooks.verify(body, hmac.new(b"whsec", body.encode(), hashlib.sha256).hexdigest(), "whsec"))
        self.assertFalse(webhooks.verify(body, hmac.new(b"other", body.encode(), hashlib.sha256).hexdigest(), "whsec"))


@unittest.skipUnless(os.environ.get("AFROPIN_TEST_ENV"), "set AFROPIN_TEST_ENV to run against an API")
class Live(unittest.TestCase):
    def test_round_trip_in_test_mode(self):
        env = json.load(open(os.environ["AFROPIN_TEST_ENV"]))
        reseller = Client(env["reseller"]["key_id"], env["reseller"]["secret"], base_url=env["base_url"])
        brand = Client(env["brand"]["key_id"], env["brand"]["secret"], base_url=env["base_url"])

        self.assertTrue(len(reseller.reseller.wallets.list()) > 0)
        catalog = reseller.reseller.catalog.list({"limit": 5})
        self.assertIsInstance(catalog, Page)
        self.assertTrue(len(catalog) > 0 and catalog.paging["total"] > 0)
        product = reseller.reseller.catalog.get(env["catalog_id"])
        amount = float((product.get("denominations") or [product["min"]])[0])
        sold = reseller.reseller.pins.sell({
            "catalog_id": env["catalog_id"], "amount": amount, "external_reference": "sdk-py-" + secrets.token_hex(6),
            "first_name": "Sdk", "last_name": "Test", "email": "sdk.test@gmail.com",
        })
        self.assertTrue(sold["pin_code"] and sold["pin_id"])
        self.assertEqual(float(reseller.reseller.pins.get(sold["pin_id"])["balance"]), amount)
        with self.assertRaises(AfroPinError) as caught:
            reseller.reseller.pins.get("00000000-0000-4000-8000-000000000000")
        self.assertEqual((caught.exception.code, caught.exception.status), ("pin_not_found", 404))
        self.assertIn("can_redeem", brand.brand.pins.check({"pin_code": env["test_pin"]}))


if __name__ == "__main__":
    unittest.main()
