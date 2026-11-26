import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


@pytest.mark.view
def test_view_product(driver):

    home_page = HomePage(driver)

    # Create explicit wait with maximum timeout of 20 seconds
    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1: NAVIGATE TO LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Open Lenskart homepage")

    # Open the Lenskart homepage using reusable POM method
    home_page.open_homepage()

    # Explicit wait:
    # Wait until the webpage is completely loaded
    wait.until(
        lambda driver:
        driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # Assertion:
    # Verify that the Lenskart homepage is displayed
    assert home_page.is_homepage_displayed(), (
        "Lenskart homepage was not displayed."
    )

    print("Lenskart homepage displayed successfully")

    # =========================================================
    # STEP 2: OPEN EYEGLASSES PRODUCT LISTING
    # =========================================================

    print("STEP 2: Open Eyeglasses product listing")

    # Explicit wait:
    # Wait until the Eyeglasses menu is visible
    wait.until(
        EC.visibility_of_element_located(
            home_page.EYEGLASSES_MENU
        )
    )

    # Explicit wait:
    # Wait until the Eyeglasses menu is clickable
    wait.until(
        EC.element_to_be_clickable(
            home_page.EYEGLASSES_MENU
        )
    )

    # Open Eyeglasses using reusable POM method
    home_page.open_eyeglasses()

    # Explicit wait:
    # Wait until the selected product is present
    wait.until(
        EC.presence_of_element_located(
            home_page.PRODUCT_IMAGE
        )
    )

    # =========================================================
    # STEP 3: VERIFY PRODUCTS ARE DISPLAYED
    # =========================================================

    print("STEP 3: Verify products are displayed")

    # Explicit wait:
    # Wait until the product is visible on the listing page
    wait.until(
        EC.visibility_of_element_located(
            home_page.PRODUCT_IMAGE
        )
    )

    # Assertion:
    # Verify that the product listing is displayed
    assert home_page.is_product_list_displayed(), (
        "Product list was not displayed."
    )

    print("Product listing displayed successfully")

    # =========================================================
    # STEP 4: CLICK THE PRODUCT
    # =========================================================

    print("STEP 4: Click product")

    # Explicit wait:
    # Wait until the selected product is clickable
    wait.until(
        EC.element_to_be_clickable(
            home_page.PRODUCT_IMAGE
        )
    )

    # Click the product using reusable POM method
    home_page.click_product()

    # Explicit wait:
    # Wait until the product-detail container is visible
    wait.until(
        EC.visibility_of_element_located(
            home_page.PRODUCT_DETAIL_CONTAINER
        )
    )

    # =========================================================
    # STEP 5: VERIFY PRODUCT DETAIL PAGE
    # =========================================================

    print("STEP 5: Verify product detail page")

    # Assertion:
    # Verify that the product-detail page is displayed
    assert home_page.is_product_detail_page_displayed(), (
        "Product detail page was not displayed."
    )

    # =========================================================
    # TEST RESULT
    # =========================================================

    print(
        "\nVIEW PRODUCT TEST PASSED: "
        "Product detail page was displayed successfully."
    )