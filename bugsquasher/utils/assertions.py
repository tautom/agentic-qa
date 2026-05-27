"""Common UI assertion helpers."""
import re

from playwright.sync_api import expect, Locator, Page


def expect_url_contains(page: Page, partial_url: str) -> None:
    expect(page).to_have_url(re.compile(f".*{re.escape(partial_url)}.*"))


def expect_text(locator: Locator, expected_text: str) -> None:
    expect(locator).to_have_text(expected_text)


def expect_visible(locator: Locator) -> None:
    expect(locator).to_be_visible()
