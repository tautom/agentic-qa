"""Pytest and Playwright fixtures for the SauceDemo framework."""
from __future__ import annotations

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from config.settings import settings as runtime_settings
from pages.cart_page import CartPage
from pages.base_page import *
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from config.settings import Settings


@pytest.fixture(scope="session")
def settings():
    return runtime_settings


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, settings):
    return {
        **browser_context_args,
        "base_url": settings.base_url,
        "viewport": {"width": 1366, "height": 768},
        "ignore_https_errors": True,
    }


@pytest.fixture
def context(browser: Browser, browser_context_args, settings) -> BrowserContext:
    context = browser.new_context(**browser_context_args)
    context.set_default_timeout(settings.default_timeout_ms)
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def logged_in_home_page(page: Page, settings: Settings) -> InventoryPage:

    login_page = LoginPage(page)
    inv_page = InventoryPage(page)
    login_page.load(settings.base_url)
    login_page.login(settings.username, settings.password)
    inv_page.assert_loaded()
    return inv_page
