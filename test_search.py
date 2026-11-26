import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


@pytest.mark.search
def test_search_for_sunglasses(driver):

    home_page = HomePage(driver)

    # Create explicit wait with maximum timeout of 20 seconds
    wait = WebDriverWait(driver, 20)

    # =========================================================
    # STEP 1: NAVIGATE TO LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Navigate to Lenskart homepage")

    # Open the Lenskart homepage using the reusable POM method
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
    # STEP 2: WAIT FOR SEARCH BUTTON
    # =========================================================

    print("STEP 2: Wait for Search button")

    # Explicit wait:
    # Wait until the Search button is visible
    wait.until(
        EC.visibility_of_element_located(
            home_page.SEARCH_BUTTON
        )
    )

    # Explicit wait:
    # Wait until the Search button is clickable
    wait.until(
        EC.element_to_be_clickable(
            home_page.SEARCH_BUTTON
        )
    )

    print("Search button is visible and clickable")

    # =========================================================
    # STEP 3: ENTER "SUNGLASSES" IN SEARCH FIELD
    # =========================================================

    print("STEP 3: Enter Sunglasses in search field")

    # Reusable POM method:
    # Opens the Search dialog and enters Sunglasses
    entered_value = home_page.enter_search_term(
        "Sunglasses"
    )

    # Explicit wait:
    # Wait until the Search input contains Sunglasses
    wait.until(
        lambda driver:
        driver.find_element(
            *home_page.SEARCH_INPUT
        ).get_attribute("value") == "Sunglasses"
    )

    # Assertion:
    # Verify that Sunglasses was entered correctly
    assert entered_value == "Sunglasses", (
        f"Expected Sunglasses but found {entered_value}"
    )

    print("Sunglasses entered successfully")

    # =========================================================
    # STEP 4: SUBMIT THE SEARCH
    # =========================================================

    print("STEP 4: Submit search")

    # Explicit wait:
    # Wait until the Search input is clickable
    wait.until(
        EC.element_to_be_clickable(
            home_page.SEARCH_INPUT
        )
    )

    # Reusable POM method:
    # Press Enter to submit the search
    home_page.submit_search()

    print("Search submitted")

    # =========================================================
    # STEP 5: WAIT FOR SEARCH RESULTS
    # =========================================================

    print("STEP 5: Wait for Sunglasses search results")

    # Explicit wait:
    # Wait until the URL or page content indicates
    # that Sunglasses search results are displayed
    wait.until(
        lambda driver:
        "sunglasses" in driver.current_url.lower()
        or
        "sunglasses" in driver.page_source.lower()
    )

    # =========================================================
    # STEP 6: VERIFY SEARCH RESULTS
    # =========================================================

    print("STEP 6: Verify Sunglasses search results")

    # Assertion:
    # Verify that search results are displayed
    assert home_page.are_search_results_displayed(), (
        "Search results for Sunglasses were not displayed."
    )

    print(
        "\nSEARCH TEST PASSED: "
        "Search results for Sunglasses were displayed successfully."
    )