"""Page object for the SauceDemo cart page."""
from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    URL_FRAGMENT = "cart.html"
    TITLE = "[data-test='title']"
    CART_ITEM = "[data-test='inventory-item']"
    CART_ITEM_NAME = "[data-test='inventory-item-name']"
    CART_ITEM_PRICE = "[data-test='inventory-item-price']"
    CHECKOUT_BUTTON = "#checkout"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"

    def assert_loaded(self) -> None:
        expect(self.page.locator(self.TITLE)).to_have_text("Your Cart")
        self.assert_url_contains(self.URL_FRAGMENT)

    def item_names(self) -> list[str]:
        return self.page.locator(self.CART_ITEM_NAME).all_inner_texts()

    def item_prices(self) -> list[str]:
        return self.page.locator(self.CART_ITEM_PRICE).all_inner_texts()

    def assert_product_in_cart(self, product_name: str) -> None:
        expect(self.page.locator(self.CART_ITEM).filter(has_text=product_name)).to_be_visible()

    def remove_product_by_name(self, product_name: str) -> None:
        cart_item = self.page.locator(self.CART_ITEM).filter(has_text=product_name)
        expect(cart_item).to_be_visible()
        cart_item.get_by_role("button", name="Remove").click()

    def continue_shopping(self) -> None:
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()

    def checkout(self) -> None:
        self.page.locator(self.CHECKOUT_BUTTON).click()
