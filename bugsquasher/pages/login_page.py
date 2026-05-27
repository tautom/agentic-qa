"""Page object for SauceDemo login page."""
from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def load(self, base_url: str) -> "LoginPage":
        self.open(base_url)
        expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible()
        return self

    def login(self, username: str, password: str) -> None:
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def assert_error_message_contains(self, expected_text: str) -> None:
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(expected_text)
