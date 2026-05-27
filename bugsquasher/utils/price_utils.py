"""Helpers for price calculations in cart and checkout assertions."""
from decimal import Decimal


def price_text_to_decimal(price_text: str) -> Decimal:
    return Decimal(price_text.replace("$", "").strip())


def sum_prices(price_texts: list[str]) -> Decimal:
    return sum((price_text_to_decimal(price) for price in price_texts), Decimal("0.00"))
