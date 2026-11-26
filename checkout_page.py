from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # =========================================================
    # CHECKOUT LOCATORS
    # =========================================================

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains("
        "translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz',"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
        "'CHECKOUT')]"
    )

    CHECKOUT_LINK = (
        By.XPATH,
        "//a[contains("
        "translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz',"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
        "'CHECKOUT')]"
    )

    CHECKOUT_TEXT = (
        By.XPATH,
        "//*[contains("
        "translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz',"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
        "'CHECKOUT')]"
    )

    # =========================================================
    # VERIFY CHECKOUT BUTTON
    # =========================================================

    def is_checkout_available(self):

        print("Checking Checkout option...")

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    self.CHECKOUT_BUTTON
                )
            )

            print("Checkout button displayed")

            return True

        except TimeoutException:

            try:

                self.wait.until(
                    EC.visibility_of_element_located(
                        self.CHECKOUT_LINK
                    )
                )

                print("Checkout link displayed")

                return True

            except TimeoutException:

                return False

    # =========================================================
    # CLICK CHECKOUT
    # =========================================================

    def click_checkout(self):

        print("Clicking Checkout...")

        try:

            self.safe_click(
                self.CHECKOUT_BUTTON
            )

        except TimeoutException:

            try:

                self.safe_click(
                    self.CHECKOUT_LINK
                )

            except TimeoutException:

                self.safe_click(
                    self.CHECKOUT_TEXT
                )

        print("Checkout clicked")

    # =========================================================
    # VERIFY CHECKOUT NAVIGATION
    # =========================================================

    def is_checkout_stage_displayed(self):

        print("Checking checkout navigation...")

        try:

            self.wait.until(
                lambda driver:
                "checkout" in driver.current_url.lower()
                or
                "checkout" in driver.page_source.lower()
            )

            return True

        except TimeoutException:

            return False