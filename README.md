# AfroPin for Python

The AfroPin gift card API from Python: sell, top up and redeem PINs, quotes, stores and webhooks.

```
pip install afropin
```

Python 3.8 or newer. No dependencies.

## Start

```python
import os
from afropin import Client

afropin = Client(os.environ["AFROPIN_KEY_ID"], os.environ["AFROPIN_SECRET"])
```

Your API key's mode decides whether you work with test or live records; the address is the same for both. Keep the
secret on your server, never in a browser or app.

### Reseller: sell a PIN

```python
pin = afropin.reseller.pins.sell({
    "catalog_id": catalog_id,         # from afropin.reseller.catalog.list()
    "amount": 5000,
    "external_reference": order_id,   # your own reference; reusing it fails safely
    "first_name": "Ada",
    "last_name": "Obi",
    "email": "ada@example.com",
})

pin["pin_code"]   # the full code: returned only here, so deliver it to your customer now
```

### Brand: check and redeem a PIN

```python
check = afropin.brand.pins.check({"pin_code": code, "amount": 2500})
if check["can_redeem"]:
    afropin.brand.pins.redeem({"pin_code": code, "amount": 2500, "external_reference": sale_id})
```

Methods use snake_case (`top_up`, `new_code`, `wallet_links`); every call is listed in [METHODS.md](../METHODS.md).
Parameters and response fields are the API's own, as in the developer docs.

## Errors

```python
from afropin import AfroPinError

try:
    afropin.reseller.pins.top_up({"pin_id": pin_id, "amount": 1000, "external_reference": ref})
except AfroPinError as error:
    error.code    # for example pin_not_found, amount_too_large, duplicate_external_reference
    error.fields  # per-field messages for input problems
    error.status  # HTTP status, or 0 when the API wasn't reached (connection_failed)
```

Branch on `code`; the message is for people and may change.

## Lists

Lists return a `Page`: iterate it, and read `paging` for `page`, `pages` and `total`.

```python
page = afropin.brand.payments.list({"limit": 50})
for payment in page:
    ...
if page.has_more:
    following = afropin.brand.payments.list({"limit": 50, "page": page.paging["page"] + 1})
```

## Idempotency and retries

Each request gets a new `Idempotency-Key`. To use your own: `sell(params, idempotency_key=key)`. Nothing is retried for
you. If a sale times out, send it again with the same `external_reference`: it either goes through once, or fails with
`duplicate_external_reference`.

## Webhooks

```python
from afropin import webhooks

# Flask
event = webhooks.parse(request.get_data(), request.headers.get("webhook-secret"), WEBHOOK_SECRET)
if event["type"] == "pin.spent":
    ...
```

`parse` raises `invalid_signature` when the signature doesn't match. Use the raw body exactly as received.
