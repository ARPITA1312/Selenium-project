import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


@pytest.mark.filter
def test_filter_by_men(driver):

    home_page = HomePage(driver)

    # =========================================================
    # EXPLICIT WAIT
    # =========================================================

    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1: NAVIGATE TO LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Navigate to Lenskart homepage")

    home_page.open_homepage()

    # Explicit wait:
    # Wait until the webpage has completely loaded.
    wait.until(
        lambda driver:
        driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # Assertion:
    # Verify that the Lenskart homepage is displayed.
    assert home_page.is_homepage_displayed(), (
        "Lenskart homepage was not displayed."
    )

    print("Lenskart homepage displayed successfully")

    # =========================================================
    # STEP 2: WAIT FOR MEN FILTER
    # =========================================================

    print("STEP 2: Wait for Men filter")

    # Explicit wait:
    # Wait until the Men filter is visible.
    wait.until(
        EC.visibility_of_element_located(
            home_page.MEN_FILTER
        )
    )

    # Explicit wait:
    # Wait until the Men filter is clickable.
    wait.until(
        EC.element_to_be_clickable(
            home_page.MEN_FILTER
        )
    )

    print("Men filter is visible and clickable")

    # =========================================================
    # STEP 3: SELECT MEN FILTER
    # =========================================================

    print("STEP 3: Select Men filter")

    # Reusable POM method from HomePage.
    home_page.select_men_filter()

    print("Men filter clicked")

    # =========================================================
    # STEP 4: WAIT FOR FILTER TO BE APPLIED
    # =========================================================

    print("STEP 4: Wait for Men filter to be applied")

    # Explicit wait:
    # Wait until the application indicates that
    # the Men filter has been applied.
    wait.until(
        lambda driver:
        home_page.is_men_filter_applied()
    )

    # =========================================================
    # STEP 5: VERIFY MEN FILTER
    # =========================================================

    print("STEP 5: Verify Men filter")

    # Assertion:
    # Verify that the Men filter was applied successfully.
    assert home_page.is_men_filter_applied(), (
        "Men filter was not applied successfully."
    )

    print(
        "\nFILTER TEST PASSED: "
        "Men filter was applied successfully."
    )