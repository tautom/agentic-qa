"""Base page object with cross-page behavior."""
from __future__ import annotations

import re

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def wait_for_page_ready(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")

    def assert_url_contains(self, path_fragment: str) -> None:
        expect(self.page).to_have_url(re.compile(f".*{re.escape(path_fragment)}.*"))

    def get_title(self) -> str:
        return self.page.title()
