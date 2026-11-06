"""The AfroPin gift card API. See https://afropin.com/user/docs for every endpoint and field."""

from .client import BASE_URL, VERSION, Client
from .errors import AfroPinError
from .page import Page
from . import webhooks

__all__ = ["Client", "AfroPinError", "Page", "webhooks", "VERSION", "BASE_URL"]
