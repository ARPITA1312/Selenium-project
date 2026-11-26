import pytest

from selenium.webdriver.support.ui import WebDriverWait

from pages.home_page import HomePage


@pytest.mark.view
@pytest.mark.negative
def test_view_invalid_product(driver):

    home_page = HomePage(driver)

    # Create explicit wait with maximum timeout of 20 seconds
    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1: NAVIGATE TO LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Open Lenskart homepage")

    # Open Lenskart homepage using reusable POM method
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
    # Verify that Lenskart homepage is displayed
    assert home_page.is_homepage_displayed(), (
        "Lenskart homepage was not displayed."
    )

    print("Lenskart homepage displayed successfully")

    # =========================================================
    # STEP 2: OPEN INTENTIONALLY INVALID PRODUCT
    # =========================================================

    print("STEP 2: Open intentionally invalid product")

    # Store current URL before opening invalid product
    previous_url = driver.current_url

    # Open invalid product using reusable POM method
    home_page.open_invalid_product()

    # Explicit wait:
    # Wait until navigation from the homepage occurs
    wait.until(
        lambda driver:
        driver.current_url != previous_url
    )

    # Explicit wait:
    # Wait until the new page has completely loaded
    wait.until(
        lambda driver:
        driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    print("Invalid product request processed")

    # =========================================================
    # STEP 3: VERIFY VALID PRODUCT PAGE IS NOT DISPLAYED
    # =========================================================

    print(
        "STEP 3: Verify normal product-detail "
        "page is not displayed"
    )

    # Explicit wait:
    # Wait until the existing POM validation confirms
    # that this is not a valid product-detail page
    wait.until(
        lambda driver:
        not home_page.is_valid_product_detail_displayed()
    )

    # Assertion:
    # Invalid product must not display a normal
    # valid product-detail page
    assert not home_page.is_valid_product_detail_displayed(), (
        "A valid product-detail page was unexpectedly "
        "displayed for an invalid product."
    )

    # =========================================================
    # TEST RESULT
    # =========================================================

    print(
        "\nNEGATIVE VIEW PRODUCT TEST PASSED: "
        "A valid product-detail page was not displayed "
        "for the invalid product."
    )