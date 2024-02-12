class AddToCartPage:
    def __init__(self, page):
        self.txtLegendOfZelda = page.get_by_role("heading", name="The Legend of Zelda™: Tears").first
        self.txtQTY = page.get_by_text("Qty: 1", exact=True).first
        self.txtPrice = page.get_by_text("$69.99", exact=True).first
        self.btnViewCartAndCheckout = page.get_by_role("link", name="View cart and check out")
