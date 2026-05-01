class CartPage:
    def __init__(self, page):
        self.page = page
    def continue_shopping(self):
        self.page.click("#continue-shopping")
    def remove_item(self, item_name):
        self.page.click(f"#remove-{item_name}")
    def go_to_checkout(self):
        self.page.click("#checkout")