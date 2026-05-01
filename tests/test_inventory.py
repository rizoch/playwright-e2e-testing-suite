from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def login_sequence(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url
    inventory = InventoryPage(page)
    return inventory

def test_add_to_cart(page):
    inventory = login_sequence(page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").inner_text() == '1'

def test_remove_from_cart(page):
    inventory = login_sequence(page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").inner_text() == '1'
    inventory.remove_from_cart("sauce-labs-backpack")
    assert page.locator("[data-test='shopping-cart-badge']").is_hidden()

def test_go_to_cart(page):
    inventory = login_sequence(page)
    inventory.go_to_cart()
    assert "cart" in page.url

def test_sort_by(page):
    inventory = login_sequence(page)
    inventory.sort_by("za")
    assert page.locator("[data-test='active-option']").inner_text() == 'Name (Z to A)'
    inventory.sort_by("lohi")
    assert page.locator("[data-test='active-option']").inner_text() == 'Price (low to high)'
