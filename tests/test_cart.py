from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

expected = {
    "Sauce Labs Backpack": {
        "price": "$29.99",
        "quantity": "1"
    },
    "Sauce Labs Bike Light": {
        "price": "$9.99",
        "quantity": "1"
    }
}

def startup_sequence(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url
    inventory = InventoryPage(page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    inventory.go_to_cart()
    cart = CartPage(page)
    return cart

def test_items_in_cart(page):
    cart = startup_sequence(page)
    cart_list = page.locator("[data-test='cart-list']")
    cart_items = cart_list.locator("[data-test='inventory-item']")
    assert cart_items.count() == len(expected)
    for i in range(cart_items.count()):
        item = cart_items.nth(i)
        quantity = item.locator("[data-test='item-quantity']").inner_text()
        name = item.locator("[data-test='inventory-item-name']").inner_text()
        price = item.locator("[data-test='inventory-item-price']").inner_text()

        assert name in expected
        assert quantity == expected[name].get("quantity")
        assert price == expected[name].get("price")

def test_items_removed(page):
    cart = startup_sequence(page)
    cart_list = page.locator("[data-test='cart-list']")
    cart_items = cart_list.locator("[data-test='inventory-item']")
    cart.remove_item("sauce-labs-backpack")
    assert cart_items.count() == len(expected) - 1
    assert "Sauce Labs Backpack" not in cart_items.locator("[data-test='inventory-item-name']").all_inner_texts()
    for i in range(cart_items.count()):
        item = cart_items.nth(i)
        assert item.locator("[data-test='inventory-item-name']").inner_text() in expected

def test_continue_shopping(page):
    cart = startup_sequence(page)
    cart.continue_shopping()
    assert "inventory" in page.url

def test_go_to_checkout(page):
    cart = startup_sequence(page)
    cart.go_to_checkout()
    assert "checkout" in page.url