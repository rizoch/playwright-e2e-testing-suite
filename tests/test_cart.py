from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def login_sequence(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url
    inventory = InventoryPage(page)
    return inventory

##TODO: test adding item to cart, verifying it's in the cart and no other items are. verify remove works. verify going back to shopping then back to cart and item exists
##TODO: verify checkout button works