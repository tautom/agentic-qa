import re
from playwright.sync_api import Page, expect
from pages.base_page import *
from pages.login_page import *
from config.settings import *
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



USERNAME = "standard_user"
PASSWORD = "secret_sauce"

    

def test_addtocart(logged_in_home_page ):

    inv_page = logged_in_home_page
    inv_page.add_backpack_to_cart()
    assert inv_page.cart_badge_count() == 1
    

def test_checkout(logged_in_home_page):

    inv_page = logged_in_home_page
    inv_page.add_backpack_to_cart()
    inv_page.go_to_cart()    

    cart_page = CartPage(inv_page.page)
    checkout_page = CheckoutPage(inv_page.page)

    cart_page.checkout()
    checkout_page.submit_customer_information("tester", "qa", "94006")
    checkout_page.assert_overview_loaded()
    checkout_page.finish_order()
    checkout_page.assert_order_complete()