"""Page object for All Items / Products inventory page."""
from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL_FRAGMENT = "inventory.html"
    TITLE = "[data-test='title']"
    INVENTORY_ITEM = "[data-test='inventory-item']"
    INVENTORY_ITEM_NAME = "[data-test='inventory-item-name']"
    INVENTORY_ITEM_PRICE = "[data-test='inventory-item-price']"
    SHOPPING_CART_LINK = "[data-test='shopping-cart-link']"
    SHOPPING_CART_BADGE = "[data-test='shopping-cart-badge']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    INVENTORY_ITEM_BACKPACK = "[data-test='add-to-cart-sauce-labs-backpack']"

    def assert_loaded(self) -> None:
        expect(self.page.locator(self.TITLE)).to_have_text("Products")
        self.assert_url_contains(self.URL_FRAGMENT)

    def product_cards(self):
        return self.page.locator(self.INVENTORY_ITEM)

    def product_names(self) -> list[str]:
        return self.page.locator(self.INVENTORY_ITEM_NAME).all_inner_texts()

    def product_prices(self) -> list[str]:
        return self.page.locator(self.INVENTORY_ITEM_PRICE).all_inner_texts()

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        product = self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name)
        expect(product).to_be_visible()
        product.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart_by_name(self, product_name: str) -> None:
        product = self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name)
        expect(product).to_be_visible()
        product.get_by_role("button", name="Remove").click()

    def cart_badge_count(self) -> int:
        badge = self.page.locator(self.SHOPPING_CART_BADGE)
        if badge.count() == 0:
            return 0
        return int(badge.inner_text())

    def go_to_cart(self) -> None:
        self.page.locator(self.SHOPPING_CART_LINK).click()

    def sort_products(self, option_label: str) -> None:
        self.page.locator(self.SORT_DROPDOWN).select_option(label=option_label)

    def add_backpack_to_cart(self):
        self.page.locator(self.INVENTORY_ITEM_BACKPACK).click()
