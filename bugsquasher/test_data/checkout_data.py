"""Checkout form data objects."""
from dataclasses import dataclass


@dataclass(frozen=True)
class CheckoutInfo:
    first_name: str
    last_name: str
    postal_code: str


VALID_CHECKOUT_INFO = CheckoutInfo(
    first_name="Automation",
    last_name="Tester",
    postal_code="12345",
)
