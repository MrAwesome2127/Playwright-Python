class CheckoutPage:
    def __init__(self, page):
        self.txtCongratulations = page.get_by_text("Congratulations you've qualified for free shipping!").nth(1)
        self.txtQtyInCart = page.locator("#main").get_by_text("1", exact=True)
        self.txtOrderSummary = page.get_by_text("Order summary")
        self.txtPromotionalCode = page.get_by_role("button", name="Promotional code")
        self.txtItemsSubTotal = page.get_by_text("Item(s) subtotal")
        self.txtPrice = page.get_by_text("$69.99", exact=True).nth(2)
        self.txtShipping = page.get_by_text("Shipping", exact=True)
        self.txtShippingFee = page.get_by_text("Free", exact=True)
        self.txtEstimatedTax = page.get_by_text("Estimated tax")
        self.txtEstimatedTaxPrice = page.get_by_text("$0.00", exact=True)
        self.txtEstimatedTotal = page.get_by_text("Estimated total", exact=True)
        self.txtEstimatedTotalPrice = page.get_by_text("$69.99", exact=True).nth(3)