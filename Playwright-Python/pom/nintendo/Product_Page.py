class ProductPage:
    def __init__(self, page):
        self.rdoPhysical = page.get_by_label("Physical The Legend of Zelda™: Tears of the Kingdom $")
        self.btnAddToCart = page.get_by_role("button", name="Add to cart")
