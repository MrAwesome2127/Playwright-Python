class MerchandisePage:
    def __int__(self, page):
        self.lnkSWAGShopLegendOfZelda = page.get_by_role("link", name="Shop The Legend of Zelda")
