import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def login_sequence(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url
    return login

def test_add_to_cart(page):
    login_sequence(page)
    inventory = InventoryPage(page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").inner_text() == '1'

def test_remove_from_cart(page):
    login_sequence(page)
    inventory = InventoryPage(page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").inner_text() == '1'
    inventory.remove_from_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").is_hidden()

def go_to_cart(page):
    login_sequence(page)
    inventory = InventoryPage(page)
    



