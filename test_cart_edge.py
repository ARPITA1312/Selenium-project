import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.product_page import ProductPage


@pytest.mark.edge
@pytest.mark.cart
def test_rapid_double_click_does_not_break_cart_flow(driver):

    product_page = ProductPage(driver)

    # Create an explicit wait of 20 seconds
    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1: NAVIGATE TO THE LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Open Lenskart homepage")

    # Open the Lenskart homepage
    product_page.open_homepage()

    # Explicit wait:
    # Wait until the webpage is completely loaded
    wait.until(
        lambda driver:
        driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # =========================================================
    # STEP 2: CLICK THE EYEGLASSES OPTION
    # =========================================================

    print("STEP 2: Click Eyeglasses")

    # Explicit wait:
    # Wait until the Eyeglasses menu is clickable
    wait.until(
        EC.element_to_be_clickable(
            product_page.EYEGLASSES_MENU
        )
    )

    # Click the Eyeglasses menu
    product_page.click_eyeglasses()

    # Explicit wait:
    # Wait until the product listing is available
    wait.until(
        EC.presence_of_element_located(
            product_page.PRODUCT_IMAGE
        )
    )

    # =========================================================
    # STEP 3: SELECT A PRODUCT FROM THE PRODUCT LIST
    # =========================================================

    print("STEP 3: Click product using XPath")

    # Explicit wait:
    # Wait until the selected product is clickable
    wait.until(
        EC.element_to_be_clickable(
            product_page.PRODUCT_IMAGE
        )
    )

    # Click the selected product
    product_page.click_product()

    # Explicit wait:
    # Wait until the product-detail page is visible
    wait.until(
        EC.visibility_of_element_located(
            product_page.PRODUCT_DETAIL_CONTAINER
        )
    )

    # =========================================================
    # STEP 4: VERIFY THE PRODUCT-DETAIL PAGE
    # =========================================================

    print("STEP 4: Verify product-detail page")

    # Assertion:
    # Verify that the product-detail page is displayed
    assert product_page.is_product_detail_page_displayed(), (
        "Product-detail page was not displayed."
    )

    # =========================================================
    # STEP 5: CLICK SELECT LENSES
    # =========================================================

    print("STEP 5: Click Select Lenses")

    # Explicit wait:
    # Wait until Select Lenses is clickable
    wait.until(
        EC.element_to_be_clickable(
            product_page.SELECT_LENSES_BUTTON
        )
    )

    # Click Select Lenses
    product_page.click_select_lenses()

    # Explicit wait:
    # Wait until the Select Lens Type dialog is visible
    wait.until(
        EC.visibility_of_element_located(
            product_page.LENS_TYPE_DIALOG
        )
    )

    # Assertion:
    # Verify that the Select Lens Type dialog is displayed
    assert product_page.is_lens_type_dialog_displayed(), (
        "Select Lens Type dialog was not displayed."
    )

    # =========================================================
    # STEP 6: SELECT ZERO POWER
    # =========================================================

    print("STEP 6: Select Zero Power")

    # Explicit wait:
    # Wait until the Zero Power option is present
    wait.until(
        EC.presence_of_element_located(
            product_page.ZERO_POWER_OPTION
        )
    )

    # Select Zero Power
    product_page.select_zero_power()

    # Explicit wait:
    # Wait until the Choose Lens Package dialog is displayed
    wait.until(
        EC.visibility_of_element_located(
            product_page.LENS_PACKAGE_DIALOG
        )
    )

    # =========================================================
    # STEP 7: SELECT BLU SCREEN LENSES
    # =========================================================

    print("STEP 7: Select BLU Screen package")

    # Explicit wait:
    # Wait until BLU Screen package is available
    wait.until(
        EC.presence_of_element_located(
            product_page.BLU_SCREEN_PACKAGE
        )
    )

    # Select BLU Screen Lenses
    product_page.select_blu_screen_package()

    # Explicit wait:
    # Wait until Select This Lens button is visible
    wait.until(
        EC.visibility_of_element_located(
            product_page.SELECT_THIS_LENS_BUTTON
        )
    )

    # =========================================================
    # STEP 8: PERFORM THE EDGE CASE
    # RAPIDLY CLICK "SELECT THIS LENS" TWICE
    # =========================================================

    print(
        "STEP 8: Rapidly click Select This Lens twice"
    )

    # Explicit wait:
    # Wait until Select This Lens is clickable
    wait.until(
        EC.element_to_be_clickable(
            product_page.SELECT_THIS_LENS_BUTTON
        )
    )

    # Edge-case action:
    # Rapidly click Select This Lens two times
    product_page.rapid_double_click_select_this_lens()

    # =========================================================
    # STEP 9: VERIFY THAT THE CART IS DISPLAYED
    # =========================================================

    print("STEP 9: Verify cart")

    # Wait for the cart to open automatically
    cart_displayed = product_page.wait_for_cart()

    # If the cart does not open automatically,
    # wait for the cart icon and open it manually
    if not cart_displayed:

        # Explicit wait:
        # Wait until the cart icon is clickable
        wait.until(
            EC.element_to_be_clickable(
                product_page.CART_ICON
            )
        )

        # Open the cart
        cart_displayed = product_page.open_cart()

    # Assertion:
    # Verify that the cart is displayed even after
    # rapidly clicking Select This Lens twice
    assert cart_displayed, (
        "EDGE TEST FAILED: "
        "Cart was not displayed after rapidly "
        "clicking Select This Lens."
    )

    # =========================================================
    # TEST RESULT
    # =========================================================

    print(
        "\nEDGE TEST PASSED: "
        "Cart was successfully displayed after "
        "rapid double-clicking Select This Lens."
    )