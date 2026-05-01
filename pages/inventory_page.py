class InventoryPage:
    def __init__(self, page):
        self.page = page
    def add_to_cart(self, item_name):
        self.page.click(f"#add-to-cart-{item_name}")
    def remove_from_cart(self, item_name):
        self.page.click(f"#remove-{item_name}")
    def go_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()
    def sort_by(self, sort_type):
        self.page.locator("[data-test='product-sort-container']").select_option(sort_type)