class HomePage:
    def __init__(self, page):
        self.btnSearch = page.get_by_role("button", name="Search")
        self.btnStore = page.get_by_role("button", name="My Nintendo Store")
        self.ddlMerchandise = page.get_by_test_id("dropdownMenu").get_by_role("link", name="Merchandise")
        self.fldSearch = page.get_by_role("textbox", name="Search games, hardware, news")
        self.imgLegendOfZelda = page.get_by_label("The Legend of Zelda™: Tears of the Kingdom", exact=True)
        self.ddlSearchCategories = (page.locator("form").
                                    filter(has_text="SearchAll categories").
                                    get_by_test_id("ChevronDownIcon"))
        self.txtMerchandise = page.locator("#react-select-2-option-3")

