import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
def test_checkout_option(driver):

    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    # Explicit wait object
    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1 - OPEN HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Open Lenskart homepage")

    product_page.open_homepage()

    # Explicit wait - wait until page is fully loaded
    wait.until(
        lambda driver:
        driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # =========================================================
    # STEP 2 - OPEN EYEGLASSES
    # =========================================================

    print("STEP 2: Open Eyeglasses")

    # Explicit wait for Eyeglasses menu
    wait.until(
        EC.element_to_be_clickable(
            product_page.EYEGLASSES_MENU
        )
    )

    product_page.click_eyeglasses()

    # Explicit wait for product
    wait.until(
        EC.presence_of_element_located(
            product_page.PRODUCT_IMAGE
        )
    )

    # =========================================================
    # STEP 3 - SELECT PRODUCT
    # =========================================================

    print("STEP 3: Select product")

    product_page.click_product()

    # Explicit wait for product detail page
    wait.until(
        EC.visibility_of_element_located(
            product_page.PRODUCT_DETAIL_CONTAINER
        )
    )

    assert (
        product_page.is_product_detail_page_displayed()
    ), (
        "Product detail page was not displayed."
    )

    # =========================================================
    # STEP 4 - SELECT LENSES
    # =========================================================

    print("STEP 4: Click Select Lenses")

    # Explicit wait for Select Lenses button
    wait.until(
        EC.element_to_be_clickable(
            product_page.SELECT_LENSES_BUTTON
        )
    )

    product_page.click_select_lenses()

    # Explicit wait for Select Lens Type dialog
    wait.until(
        EC.visibility_of_element_located(
            product_page.LENS_TYPE_DIALOG
        )
    )

    assert (
        product_page.is_lens_type_dialog_displayed()
    ), (
        "Select Lens Type dialog was not displayed."
    )

    # =========================================================
    # STEP 5 - SELECT ZERO POWER
    # =========================================================

    print("STEP 5: Select Zero Power")

    wait.until(
        EC.presence_of_element_located(
            product_page.ZERO_POWER_OPTION
        )
    )

    product_page.select_zero_power()

    # Explicit wait for lens package dialog
    wait.until(
        EC.visibility_of_element_located(
            product_page.LENS_PACKAGE_DIALOG
        )
    )

    # =========================================================
    # STEP 6 - SELECT BLU SCREEN LENSES
    # =========================================================

    print("STEP 6: Select BLU Screen Lenses")

    wait.until(
        EC.presence_of_element_located(
            product_page.BLU_SCREEN_PACKAGE
        )
    )

    product_page.select_blu_screen_package()

    # Explicit wait for Select This Lens
    wait.until(
        EC.visibility_of_element_located(
            product_page.SELECT_THIS_LENS_BUTTON
        )
    )

    # =========================================================
    # STEP 7 - SELECT THIS LENS
    # =========================================================

    print("STEP 7: Click Select This Lens")

    wait.until(
        EC.element_to_be_clickable(
            product_page.SELECT_THIS_LENS_BUTTON
        )
    )

    product_page.click_select_this_lens()

    # =========================================================
    # STEP 8 - OPEN CART
    # =========================================================

    print("STEP 8: Open Cart")

    cart_displayed = product_page.wait_for_cart()

    if not cart_displayed:

        wait.until(
            EC.element_to_be_clickable(
                product_page.CART_ICON
            )
        )

        cart_displayed = product_page.open_cart()

    assert cart_displayed, (
        "Cart was not displayed after selecting the lens."
    )

    # =========================================================
    # STEP 9 - VERIFY CHECKOUT OPTION
    # =========================================================

    print("STEP 9: Verify Checkout option")

    assert (
        checkout_page.is_checkout_available()
    ), (
        "Checkout option was not displayed in the cart."
    )

    # =========================================================
    # STEP 10 - CLICK CHECKOUT
    # =========================================================

    print("STEP 10: Click Checkout")

    checkout_page.click_checkout()

    # =========================================================
    # STEP 11 - VERIFY CHECKOUT STAGE
    # =========================================================

    print("STEP 11: Verify checkout stage")

    # Explicit wait for checkout navigation
    wait.until(
        lambda driver:
        "checkout" in driver.current_url.lower()
        or
        "checkout" in driver.page_source.lower()
    )

    assert (
        checkout_page.is_checkout_stage_displayed()
    ), (
        "Checkout stage was not displayed "
        "after clicking Checkout."
    )

    print(
        "\nCHECKOUT TEST PASSED"
    )