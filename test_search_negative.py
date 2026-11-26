import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


@pytest.mark.search
@pytest.mark.negative
def test_search_invalid_product(driver):

    home_page = HomePage(driver)

    # Test data
    invalid_search_term = "xyzabc999999"

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
    # STEP 3: ENTER INVALID / NON-EXISTING PRODUCT
    # =========================================================

    print(
        "STEP 3: Enter invalid product: "
        f"{invalid_search_term}"
    )

    # Reusable POM method:
    # Open the Search dialog and enter invalid search data
    entered_value = home_page.enter_search_term(
        invalid_search_term
    )

    # Explicit wait:
    # Wait until the entered value appears in the Search input
    wait.until(
        lambda driver:
        driver.find_element(
            *home_page.SEARCH_INPUT
        ).get_attribute("value")
        == invalid_search_term
    )

    # Assertion:
    # Verify that the invalid search term was entered correctly
    assert entered_value == invalid_search_term, (
        f"Expected '{invalid_search_term}' "
        f"but found '{entered_value}'."
    )

    print("Invalid search term entered successfully")

    # =========================================================
    # STEP 4: SUBMIT THE INVALID SEARCH
    # =========================================================

    print("STEP 4: Submit invalid search")

    # Explicit wait:
    # Wait until the Search input is clickable
    wait.until(
        EC.element_to_be_clickable(
            home_page.SEARCH_INPUT
        )
    )

    # Submit the search using reusable POM method
    home_page.submit_search()

    print("Invalid search submitted")

    # =========================================================
    # STEP 5: WAIT FOR NO-RESULTS STATE
    # =========================================================

    print("STEP 5: Wait for no-results state")

    # Explicit wait:
    # Wait until HomePage confirms that the invalid
    # search has reached a no-results/rejected state
    wait.until(
        lambda driver:
        home_page.is_invalid_search_rejected()
    )

    # =========================================================
    # STEP 6: VERIFY INVALID SEARCH IS REJECTED
    # =========================================================

    print("STEP 6: Verify no matching products are displayed")

    # Assertion:
    # Verify that the application displays the expected
    # no-results state for the invalid search term
    assert home_page.is_invalid_search_rejected(), (
        "Expected a no-results state for the invalid "
        "search term, but it was not displayed."
    )

    # =========================================================
    # TEST RESULT
    # =========================================================

    print(
        "\nNEGATIVE SEARCH TEST PASSED: "
        "The invalid product search correctly "
        "resulted in a no-results state."
    )