# Generated from sdks/spec/endpoints.json by sdks/spec/generate.py. Don't edit by hand: change the spec and run it again.

"""Every AfroPin API call, by account type and area."""


class ResellerWallets:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Your wallets and their balances, one per currency. (GET /api/v1/reseller/wallets)"""
        return self._client.request("GET", "reseller/wallets", params, idempotency_key, list_=True)


class ResellerStores:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Your stores. (GET /api/v1/reseller/stores)"""
        return self._client.request("GET", "reseller/stores", params, idempotency_key, list_=True)

    def create(self, params=None, idempotency_key=None):
        """Add a store. (POST /api/v1/reseller/stores)"""
        return self._client.request("POST", "reseller/stores", params, idempotency_key)

    def update(self, store_id, params=None, idempotency_key=None):
        """Edit a store. (POST /api/v1/reseller/stores/{store_id})"""
        return self._client.request("POST", "reseller/stores/%s" % (_quote(store_id),), params, idempotency_key)

    def delete(self, store_id, params=None, idempotency_key=None):
        """Remove a store. (DELETE /api/v1/reseller/stores/{store_id})"""
        return self._client.request("DELETE", "reseller/stores/%s" % (_quote(store_id),), params, idempotency_key)


class ResellerCards:
    def __init__(self, client):
        self._client = client

    def lookup(self, params=None, idempotency_key=None):
        """Look up one of your printed cards before activating it. (POST /api/v1/reseller/cards/lookup)"""
        return self._client.request("POST", "reseller/cards/lookup", params, idempotency_key)

    def activate(self, params=None, idempotency_key=None):
        """Activate a printed card: sells a PIN for the amount loaded. (POST /api/v1/reseller/cards/activate)"""
        return self._client.request("POST", "reseller/cards/activate", params, idempotency_key)


class ResellerCatalog:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """The products you can sell. (GET /api/v1/reseller/catalog)"""
        return self._client.request("GET", "reseller/catalog", params, idempotency_key, list_=True)

    def get(self, catalog_id, params=None, idempotency_key=None):
        """One product you can sell. (GET /api/v1/reseller/catalog/{catalog_id})"""
        return self._client.request("GET", "reseller/catalog/%s" % (_quote(catalog_id),), params, idempotency_key)


class ResellerPins:
    def __init__(self, client):
        self._client = client

    def sell(self, params=None, idempotency_key=None):
        """Sell a PIN. The response has its full code (pin_code), returned only here. (POST /api/v1/reseller/pins)"""
        return self._client.request("POST", "reseller/pins", params, idempotency_key)

    def get(self, pin_id, params=None, idempotency_key=None):
        """One of your PINs: balance, status, masks, customer, family cards. (GET /api/v1/reseller/pins/{pin_id})"""
        return self._client.request("GET", "reseller/pins/%s" % (_quote(pin_id),), params, idempotency_key)

    def movements(self, pin_id, params=None, idempotency_key=None):
        """A PIN's movements, newest first. (GET /api/v1/reseller/pins/{pin_id}/movements)"""
        return self._client.request("GET", "reseller/pins/%s/movements" % (_quote(pin_id),), params, idempotency_key, list_=True)

    def top_up(self, params=None, idempotency_key=None):
        """Add value to a PIN. (POST /api/v1/reseller/pins/top-up)"""
        return self._client.request("POST", "reseller/pins/top-up", params, idempotency_key)

    def block(self, params=None, idempotency_key=None):
        """Block (freeze) a PIN. Its cardholder can't undo it. (POST /api/v1/reseller/pins/block)"""
        return self._client.request("POST", "reseller/pins/block", params, idempotency_key)

    def unblock(self, params=None, idempotency_key=None):
        """Unblock a PIN. (POST /api/v1/reseller/pins/unblock)"""
        return self._client.request("POST", "reseller/pins/unblock", params, idempotency_key)

    def new_code(self, params=None, idempotency_key=None):
        """Give a PIN a new code; the old one stops working. (POST /api/v1/reseller/pins/new-code)"""
        return self._client.request("POST", "reseller/pins/new-code", params, idempotency_key)

    def wallet_links(self, params=None, idempotency_key=None):
        """Links that add a PIN to Google Wallet or Apple Wallet. (POST /api/v1/reseller/pins/wallet-links)"""
        return self._client.request("POST", "reseller/pins/wallet-links", params, idempotency_key)

    def set_webhook(self, params=None, idempotency_key=None):
        """Change a PIN's webhook. (POST /api/v1/reseller/pins/webhook)"""
        return self._client.request("POST", "reseller/pins/webhook", params, idempotency_key)

    def set_delivery(self, params=None, idempotency_key=None):
        """Choose who delivers a PIN's codes to its customer: us (handle_delivery true) or you. (POST /api/v1/reseller/pins/delivery)"""
        return self._client.request("POST", "reseller/pins/delivery", params, idempotency_key)

    def cashouts(self, pin_id, params=None, idempotency_key=None):
        """A PIN's cashouts. (GET /api/v1/reseller/pins/{pin_id}/cashouts)"""
        return self._client.request("GET", "reseller/pins/%s/cashouts" % (_quote(pin_id),), params, idempotency_key, list_=True)


class ResellerBrandStores:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Brand stores where your customers can spend the PINs you sell. (GET /api/v1/reseller/brand-stores)"""
        return self._client.request("GET", "reseller/brand-stores", params, idempotency_key, list_=True)


class ResellerCashouts:
    def __init__(self, client):
        self._client = client

    def request(self, params=None, idempotency_key=None):
        """Request a cashout (only while cashouts are switched on). (POST /api/v1/reseller/cashouts)"""
        return self._client.request("POST", "reseller/cashouts", params, idempotency_key)

    def send_code(self, params=None, idempotency_key=None):
        """Send the customer the confirmation code again. (POST /api/v1/reseller/cashouts/send-code)"""
        return self._client.request("POST", "reseller/cashouts/send-code", params, idempotency_key)

    def confirm(self, cashout_id, params=None, idempotency_key=None):
        """Confirm a cashout with the customer's code. (POST /api/v1/reseller/cashouts/{cashout_id}/confirm)"""
        return self._client.request("POST", "reseller/cashouts/%s/confirm" % (_quote(cashout_id),), params, idempotency_key)

    def void(self, cashout_id, params=None, idempotency_key=None):
        """Void an unpaid cashout. (POST /api/v1/reseller/cashouts/{cashout_id}/void)"""
        return self._client.request("POST", "reseller/cashouts/%s/void" % (_quote(cashout_id),), params, idempotency_key)


class Reseller:
    """The reseller API (/api/v1/reseller): every call a reseller account can make, by area."""

    def __init__(self, client):
        self.wallets = ResellerWallets(client)
        self.stores = ResellerStores(client)
        self.cards = ResellerCards(client)
        self.catalog = ResellerCatalog(client)
        self.pins = ResellerPins(client)
        self.brand_stores = ResellerBrandStores(client)
        self.cashouts = ResellerCashouts(client)


class BrandWallets:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Your wallets and their balances, one per currency. (GET /api/v1/brand/wallets)"""
        return self._client.request("GET", "brand/wallets", params, idempotency_key, list_=True)


class BrandStores:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Your stores. (GET /api/v1/brand/stores)"""
        return self._client.request("GET", "brand/stores", params, idempotency_key, list_=True)

    def create(self, params=None, idempotency_key=None):
        """Add a store. (POST /api/v1/brand/stores)"""
        return self._client.request("POST", "brand/stores", params, idempotency_key)

    def update(self, store_id, params=None, idempotency_key=None):
        """Edit a store. (POST /api/v1/brand/stores/{store_id})"""
        return self._client.request("POST", "brand/stores/%s" % (_quote(store_id),), params, idempotency_key)

    def delete(self, store_id, params=None, idempotency_key=None):
        """Remove a store. (DELETE /api/v1/brand/stores/{store_id})"""
        return self._client.request("DELETE", "brand/stores/%s" % (_quote(store_id),), params, idempotency_key)


class BrandCards:
    def __init__(self, client):
        self._client = client

    def lookup(self, params=None, idempotency_key=None):
        """Look up one of your printed cards before activating it. (POST /api/v1/brand/cards/lookup)"""
        return self._client.request("POST", "brand/cards/lookup", params, idempotency_key)

    def activate(self, params=None, idempotency_key=None):
        """Activate a printed card: sells a PIN for the amount loaded. (POST /api/v1/brand/cards/activate)"""
        return self._client.request("POST", "brand/cards/activate", params, idempotency_key)


class BrandIssuingCatalog:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """The products you can sell. (GET /api/v1/brand/issuing-catalog)"""
        return self._client.request("GET", "brand/issuing-catalog", params, idempotency_key, list_=True)

    def get(self, catalog_id, params=None, idempotency_key=None):
        """One product you can sell. (GET /api/v1/brand/issuing-catalog/{catalog_id})"""
        return self._client.request("GET", "brand/issuing-catalog/%s" % (_quote(catalog_id),), params, idempotency_key)


class BrandPins:
    def __init__(self, client):
        self._client = client

    def sell(self, params=None, idempotency_key=None):
        """Sell a PIN. The response has its full code (pin_code), returned only here. (POST /api/v1/brand/pins)"""
        return self._client.request("POST", "brand/pins", params, idempotency_key)

    def get(self, pin_id, params=None, idempotency_key=None):
        """One of your PINs: balance, status, masks, customer, family cards. (GET /api/v1/brand/pins/{pin_id})"""
        return self._client.request("GET", "brand/pins/%s" % (_quote(pin_id),), params, idempotency_key)

    def movements(self, pin_id, params=None, idempotency_key=None):
        """A PIN's movements, newest first. (GET /api/v1/brand/pins/{pin_id}/movements)"""
        return self._client.request("GET", "brand/pins/%s/movements" % (_quote(pin_id),), params, idempotency_key, list_=True)

    def top_up(self, params=None, idempotency_key=None):
        """Add value to a PIN. (POST /api/v1/brand/pins/top-up)"""
        return self._client.request("POST", "brand/pins/top-up", params, idempotency_key)

    def block(self, params=None, idempotency_key=None):
        """Block (freeze) a PIN. Its cardholder can't undo it. (POST /api/v1/brand/pins/block)"""
        return self._client.request("POST", "brand/pins/block", params, idempotency_key)

    def unblock(self, params=None, idempotency_key=None):
        """Unblock a PIN. (POST /api/v1/brand/pins/unblock)"""
        return self._client.request("POST", "brand/pins/unblock", params, idempotency_key)

    def new_code(self, params=None, idempotency_key=None):
        """Give a PIN a new code; the old one stops working. (POST /api/v1/brand/pins/new-code)"""
        return self._client.request("POST", "brand/pins/new-code", params, idempotency_key)

    def wallet_links(self, params=None, idempotency_key=None):
        """Links that add a PIN to Google Wallet or Apple Wallet. (POST /api/v1/brand/pins/wallet-links)"""
        return self._client.request("POST", "brand/pins/wallet-links", params, idempotency_key)

    def set_webhook(self, params=None, idempotency_key=None):
        """Change a PIN's webhook. (POST /api/v1/brand/pins/webhook)"""
        return self._client.request("POST", "brand/pins/webhook", params, idempotency_key)

    def set_delivery(self, params=None, idempotency_key=None):
        """Choose who delivers a PIN's codes to its customer: us (handle_delivery true) or you. (POST /api/v1/brand/pins/delivery)"""
        return self._client.request("POST", "brand/pins/delivery", params, idempotency_key)

    def check(self, params=None, idempotency_key=None):
        """Check a PIN before redeeming it; nothing changes. (POST /api/v1/brand/pins/check)"""
        return self._client.request("POST", "brand/pins/check", params, idempotency_key)

    def redeem(self, params=None, idempotency_key=None):
        """Redeem a PIN: take an amount off it and credit your wallet. (POST /api/v1/brand/pins/redeem)"""
        return self._client.request("POST", "brand/pins/redeem", params, idempotency_key)


class BrandCatalog:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """The products you accept. (GET /api/v1/brand/catalog)"""
        return self._client.request("GET", "brand/catalog", params, idempotency_key, list_=True)

    def get(self, catalog_id, params=None, idempotency_key=None):
        """One product you accept. (GET /api/v1/brand/catalog/{catalog_id})"""
        return self._client.request("GET", "brand/catalog/%s" % (_quote(catalog_id),), params, idempotency_key)


class BrandResellerStores:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Reseller stores that sell PINs you accept. (GET /api/v1/brand/reseller-stores)"""
        return self._client.request("GET", "brand/reseller-stores", params, idempotency_key, list_=True)


class BrandPayments:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """The redemptions credited to you, newest first. (GET /api/v1/brand/payments)"""
        return self._client.request("GET", "brand/payments", params, idempotency_key, list_=True)

    def get(self, transaction_ref, params=None, idempotency_key=None):
        """One redemption. (GET /api/v1/brand/payments/{transaction_ref})"""
        return self._client.request("GET", "brand/payments/%s" % (_quote(transaction_ref),), params, idempotency_key)


class BrandQuotes:
    def __init__(self, client):
        self._client = client

    def list(self, params=None, idempotency_key=None):
        """Your quotes, newest first. (GET /api/v1/brand/quotes)"""
        return self._client.request("GET", "brand/quotes", params, idempotency_key, list_=True)

    def create(self, params=None, idempotency_key=None):
        """Quote a business for your gift cards in bulk; returns a pay_url. (POST /api/v1/brand/quotes)"""
        return self._client.request("POST", "brand/quotes", params, idempotency_key)

    def get(self, quote_id, params=None, idempotency_key=None):
        """One quote, by id or QTE- reference. (GET /api/v1/brand/quotes/{quote_id})"""
        return self._client.request("GET", "brand/quotes/%s" % (_quote(quote_id),), params, idempotency_key)

    def cancel(self, quote_id, params=None, idempotency_key=None):
        """Withdraw an unpaid quote. (POST /api/v1/brand/quotes/{quote_id}/cancel)"""
        return self._client.request("POST", "brand/quotes/%s/cancel" % (_quote(quote_id),), params, idempotency_key)


class Brand:
    """The brand API (/api/v1/brand): every call a brand account can make, by area."""

    def __init__(self, client):
        self.wallets = BrandWallets(client)
        self.stores = BrandStores(client)
        self.cards = BrandCards(client)
        self.issuing_catalog = BrandIssuingCatalog(client)
        self.pins = BrandPins(client)
        self.catalog = BrandCatalog(client)
        self.reseller_stores = BrandResellerStores(client)
        self.payments = BrandPayments(client)
        self.quotes = BrandQuotes(client)


def _quote(value):
    from urllib.parse import quote

    return quote(str(value), safe="")
