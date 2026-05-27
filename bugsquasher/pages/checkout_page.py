"""Page object for checkout information, overview, and confirmation pages."""
from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage
import re


class CheckoutPage(BasePage):
    INFO_URL_FRAGMENT = "checkout-step-one.html"
    OVERVIEW_URL_FRAGMENT = "checkout-step-two.html"
    COMPLETE_URL_FRAGMENT = "checkout-complete.html"

    TITLE = "[data-test='title']"
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    FINISH_BUTTON = "#finish"
    ERROR_MESSAGE = "[data-test='error']"
    SUMMARY_SUBTOTAL = "[data-test='subtotal-label']"
    SUMMARY_TAX = "[data-test='tax-label']"
    SUMMARY_TOTAL = "[data-test='total-label']"
    COMPLETE_HEADER = "[data-test='complete-header']"
    COMPLETE_TEXT = "[data-test='complete-text']"
    BACK_HOME_BUTTON = "#back-to-products"

    def assert_information_step_loaded(self) -> None:
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Your Information")
        expect(self.page).to_have_url(lambda url: self.INFO_URL_FRAGMENT in url)

    def enter_customer_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.locator(self.FIRST_NAME_INPUT).fill(first_name)
        self.page.locator(self.LAST_NAME_INPUT).fill(last_name)
        self.page.locator(self.POSTAL_CODE_INPUT).fill(postal_code)

    def continue_to_overview(self) -> None:
        self.page.locator(self.CONTINUE_BUTTON).click()

    def submit_customer_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.enter_customer_information(first_name, last_name, postal_code)
        self.continue_to_overview()

    def assert_overview_loaded(self) -> None:
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Overview")
        

    def finish_order(self) -> None:
        self.page.locator(self.FINISH_BUTTON).click()

    def assert_order_complete(self) -> None:
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Complete!")
        expect(self.page).to_have_url(re.compile(r".*checkout-complete.*"))
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text("Thank you for your order!")

    def assert_error_message_contains(self, expected_text: str) -> None:
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(expected_text)

    def subtotal_text(self) -> str:
        return self.page.locator(self.SUMMARY_SUBTOTAL).inner_text()

    def tax_text(self) -> str:
        return self.page.locator(self.SUMMARY_TAX).inner_text()

    def total_text(self) -> str:
        return self.page.locator(self.SUMMARY_TOTAL).inner_text()

    def back_home(self) -> None:
        self.page.locator(self.BACK_HOME_BUTTON).click()
