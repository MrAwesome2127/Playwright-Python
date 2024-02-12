import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.nintendo.Home_Page import HomePage
from pom.nintendo.Product_Page import ProductPage
from pom.nintendo.AddToCart_Page import AddToCartPage
from pom.nintendo.Checkout_Page import CheckoutPage

# **** Industry Standard ****
# Create a .env file and store variable there and the .gitignore uses this as a reference in GitHub Actions
# PASSWORD = os.environ['PASSWORD']

# **** Standard ****
# # PASSWORD = Below will take the secret from either the 'utils' or from 'GitHub' secrets as _
# # _ local or remote execution of the tests.
# try:
#     PASSWORD = os.environ['PASSWORD']
# except KeyError:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD


@pytest.mark.regression
def test_add_physical_game_to_cart(set_up) -> None:
    page = set_up

    # --Home Page-------------------
    homepage = HomePage(page)
    homepage.btnSearch.click()
    homepage.fldSearch.fill("Legend of Zelda")
    homepage.imgLegendOfZelda.click()

    # --Product Page-------------------
    productpage = ProductPage(page)
    productpage.rdoPhysical.click()
    expect(productpage.btnAddToCart).to_be_visible()
    productpage.btnAddToCart.click()

    # --Add to Cart Page-------------------
    addtocartpage = AddToCartPage(page)
    expect(addtocartpage.txtLegendOfZelda).to_be_visible()
    expect(addtocartpage.txtQTY).to_be_visible()
    expect(addtocartpage.txtPrice).to_be_visible()
    addtocartpage.btnViewCartAndCheckout.click()

    # --Checkout Page-------------------
    checkoutpage = CheckoutPage(page)
    expect(checkoutpage.txtCongratulations).to_be_visible()
    expect(checkoutpage.txtQtyInCart).to_be_visible()
    expect(checkoutpage.txtOrderSummary).to_be_visible()
    expect(checkoutpage.txtPromotionalCode).to_be_visible()
    expect(checkoutpage.txtItemsSubTotal).to_be_visible()
    expect(checkoutpage.txtPrice).to_be_visible()
    expect(checkoutpage.txtShipping).to_be_visible()
    expect(checkoutpage.txtShippingFee).to_be_visible()
    expect(checkoutpage.txtEstimatedTax).to_be_visible()
    expect(checkoutpage.txtEstimatedTaxPrice).to_be_visible()
    expect(checkoutpage.txtEstimatedTotal).to_be_visible()
    expect(checkoutpage.txtEstimatedTotalPrice).to_be_visible()


@pytest.mark.regression
@pytest.mark.parametrize("merchandise, qty, price",
                         [("The Legend of Zelda™: Breath of the Wild - Daruk (Standard Edition)", "1", "$134.99"),
                          ("The Legend of Zelda: Breath of the Wild – Hylian Shield (Collector's Edition)", "1",
                           "$109.99")])
def test_add_swag_to_cart(set_up, merchandise, qty, price) -> None:
    page = set_up

    # --Home Page-------------------
    homepage = HomePage(page)
    homepage.ddlSearchCategories.click()
    homepage.txtMerchandise.click()
    homepage.btnSearch.click()
    homepage.fldSearch.fill(merchandise)
    page.get_by_label(merchandise, exact=True).click()

    # --Product Page-------------------
    productpage = ProductPage(page)
    expect(productpage.btnAddToCart).to_be_visible()
    productpage.btnAddToCart.click()

    # --Add to Cart Page-------------------
    addtocartpage = AddToCartPage(page)
    expect(page.get_by_role("heading", name=merchandise).first).to_be_visible()
    expect(page.get_by_text(qty, exact=True).first).to_be_visible()
    expect(page.get_by_text(price, exact=True).first).to_be_visible()
    addtocartpage.btnViewCartAndCheckout.click()

    # --Checkout Page-------------------
    checkoutpage = CheckoutPage(page)
    # expect(page.get_by_text(merchandise)).to_be_visible() #.filter(has_text=re.compile(r"^"+merchandise+"$"))).to_be_visible()
    expect(page.locator("#main").get_by_text(qty, exact=True)).to_be_visible()
    expect(checkoutpage.txtOrderSummary).to_be_visible()
    expect(checkoutpage.txtPromotionalCode).to_be_visible()
    expect(checkoutpage.txtItemsSubTotal).to_be_visible()
    expect(page.get_by_text(price, exact=True).nth(2)).to_be_visible()
    expect(checkoutpage.txtShipping).to_be_visible()
    expect(checkoutpage.txtShippingFee).to_be_visible()
    expect(checkoutpage.txtEstimatedTax).to_be_visible()
    expect(checkoutpage.txtEstimatedTaxPrice).to_be_visible()
    expect(checkoutpage.txtEstimatedTotal).to_be_visible()
    expect(page.get_by_text(price, exact=True).nth(3)).to_be_visible()
