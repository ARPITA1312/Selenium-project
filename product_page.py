from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)

from pages.base_page import BasePage


class ProductPage(BasePage):

    HOME_URL = "https://www.lenskart.com/"

    # =========================================================
    # HOMEPAGE AND PRODUCT LOCATORS
    # =========================================================

    EYEGLASSES_MENU = (
        By.XPATH,
        "//a[normalize-space()='Eyeglasses']"
    )

    PRODUCT_IMAGE = (
        By.XPATH,
        '//*[@id="main-content"]'
        '/div/section[2]/article[3]/div[2]/div[1]/a'
    )

    PRODUCT_DETAIL_CONTAINER = (
        By.ID,
        "main-content"
    )

    # =========================================================
    # SELECT LENSES LOCATORS
    # =========================================================

    SELECT_LENSES_BUTTON = (
        By.XPATH,
        "//button[contains("
        "translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz',"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
        "'SELECT LENSES')]"
    )

    SELECT_LENSES_TEXT = (
        By.XPATH,
        "//*[contains("
        "translate(normalize-space(.),"
        "'abcdefghijklmnopqrstuvwxyz',"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
        "'SELECT LENSES')]"
    )

    LENS_TYPE_DIALOG = (
        By.XPATH,
        "//*[contains(normalize-space(.),'Select Lens Type')]"
    )

    # =========================================================
    # ZERO POWER LOCATORS
    # =========================================================

    ZERO_POWER_OPTION = (
        By.XPATH,
        '//*[@id="main-content"]/article/div[1]/div[2]'
        '/div/div/div[2]/div[2]/div[2]/div/div[2]'
        '/div/div/div/div/div[3]'
    )

    ZERO_POWER_TEXT = (
        By.XPATH,
        "//*[normalize-space()='Zero Power']"
    )

    LENS_PACKAGE_DIALOG = (
        By.XPATH,
        "//*[contains(normalize-space(.),'Choose Lens Package')]"
    )

    # =========================================================
    # BLU SCREEN AND SELECT THIS LENS LOCATORS
    # =========================================================

    BLU_SCREEN_PACKAGE = (
        By.XPATH,
        '//*[@id="package-59fc6701e4b0e569286ac018"]'
        '/div/div[1]'
    )

    BLU_SCREEN_PACKAGE_TEXT = (
        By.XPATH,
        "//*[normalize-space()='BLU Screen Lenses']"
    )

    SELECT_THIS_LENS_BUTTON = (
        By.XPATH,
        '//*[@id="modal-portal"]'
        '/div/div/div/div[3]/div/div/button'
    )

    SELECT_THIS_LENS_TEXT = (
        By.XPATH,
        "//button[contains(normalize-space(.),'Select This Lens')]"
    )

    # =========================================================
    # CART LOCATORS
    # =========================================================

    CART_ICON = (
        By.ID,
        "desktop-home-cart-trigger"
    )

    CART_CONTENT_LOCATORS = [
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'SHOPPING CART')]"
        ),
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'YOUR CART')]"
        ),
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'CHECKOUT')]"
        )
    ]

    CART_ITEM_LOCATORS = [
        (
            By.CSS_SELECTOR,
            "[data-testid*='cart-item']"
        ),
        (
            By.CSS_SELECTOR,
            "[class*='cart-item']"
        ),
        (
            By.CSS_SELECTOR,
            "[class*='CartItem']"
        )
    ]

    # =========================================================
    # STEP 1: OPEN HOMEPAGE
    # =========================================================

    def open_homepage(self):

        print("Opening Lenskart homepage...")

        self.open_url(self.HOME_URL)

        self.wait.until(
            lambda driver:
            "lenskart.com" in driver.current_url.lower()
        )

        print("Lenskart homepage displayed")

    # =========================================================
    # STEP 2: CLICK EYEGLASSES
    # =========================================================

    def click_eyeglasses(self):

        print("Waiting for Eyeglasses menu...")

        old_url = self.driver.current_url

        self.safe_click(
            self.EYEGLASSES_MENU
        )

        print("Eyeglasses clicked")

        try:
            self.wait.until(
                EC.url_changes(old_url)
            )

        except TimeoutException:
            pass

        self.wait.until(
            EC.presence_of_element_located(
                self.PRODUCT_IMAGE
            )
        )

        print("Product listing displayed")

    # =========================================================
    # STEP 3: CLICK PRODUCT
    # =========================================================

    def click_product(self):

        print("Waiting for product...")

        product = self.wait.until(
            EC.presence_of_element_located(
                self.PRODUCT_IMAGE
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )

        old_url = self.driver.current_url

        product = self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_IMAGE
            )
        )

        try:
            product.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):
            product = self.wait.until(
                EC.presence_of_element_located(
                    self.PRODUCT_IMAGE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                product
            )

        print("Product clicked")

        try:
            self.wait.until(
                EC.url_changes(old_url)
            )

        except TimeoutException:
            pass

        self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_DETAIL_CONTAINER
            )
        )

        print("Product-detail page displayed")

    def is_product_detail_page_displayed(self):

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.PRODUCT_DETAIL_CONTAINER
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # STEP 4: CLICK SELECT LENSES
    # =========================================================

    def click_select_lenses(self):

        print("Waiting for Select Lenses...")

        try:
            self.safe_click(
                self.SELECT_LENSES_BUTTON
            )

        except TimeoutException:
            self.safe_click(
                self.SELECT_LENSES_TEXT
            )

        print("Select Lenses clicked")

        self.wait.until(
            EC.visibility_of_element_located(
                self.LENS_TYPE_DIALOG
            )
        )

        print("Select Lens Type dialog displayed")

    def is_lens_type_dialog_displayed(self):

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.LENS_TYPE_DIALOG
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # STEP 5: SELECT ZERO POWER
    # =========================================================

    def select_zero_power(self):

        print("Waiting for Zero Power option...")

        try:
            self.safe_click(
                self.ZERO_POWER_OPTION
            )

        except TimeoutException:
            self.safe_click(
                self.ZERO_POWER_TEXT
            )

        print("Zero Power selected")

        self.wait.until(
            EC.visibility_of_element_located(
                self.LENS_PACKAGE_DIALOG
            )
        )

        print("Choose Lens Package displayed")

    def is_lens_package_dialog_displayed(self):

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.LENS_PACKAGE_DIALOG
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # STEP 6: SELECT BLU SCREEN PACKAGE
    # =========================================================

    def select_blu_screen_package(self):

        print("Waiting for BLU Screen package...")

        try:
            self.safe_click(
                self.BLU_SCREEN_PACKAGE
            )

        except TimeoutException:
            self.safe_click(
                self.BLU_SCREEN_PACKAGE_TEXT
            )

        print("BLU Screen package selected")

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.SELECT_THIS_LENS_BUTTON
                )
            )

        except TimeoutException:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.SELECT_THIS_LENS_TEXT
                )
            )

        print("Select This Lens button displayed")

    # =========================================================
    # NORMAL FLOW: CLICK SELECT THIS LENS ONCE
    # =========================================================

    def click_select_this_lens(self):

        print("Waiting for Select This Lens button...")

        try:
            locator = self.SELECT_THIS_LENS_BUTTON

            button = self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )

        except TimeoutException:

            print("Trying fallback Select This Lens locator...")

            locator = self.SELECT_THIS_LENS_TEXT

            button = self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        try:
            button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):
            button = self.wait.until(
                EC.presence_of_element_located(
                    locator
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        print("Select This Lens clicked")

    # =========================================================
    # EDGE FLOW: RAPID DOUBLE-CLICK SELECT THIS LENS
    # =========================================================

    def rapid_double_click_select_this_lens(self):

        print("Waiting for Select This Lens button...")

        try:
            locator = self.SELECT_THIS_LENS_BUTTON

            button = self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            )

        except TimeoutException:

            print("Trying fallback Select This Lens locator...")

            locator = self.SELECT_THIS_LENS_TEXT

            button = self.wait.until(
                EC.visibility_of_element_located(
                    locator
                )
            )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        print("Select This Lens button found")

        self.driver.execute_script(
            """
            arguments[0].click();
            arguments[0].click();
            """,
            button
        )

        print("Select This Lens clicked twice rapidly")

    # =========================================================
    # CART VERIFICATION
    # =========================================================

    def is_cart_content_visible(self):

        for locator in self.CART_CONTENT_LOCATORS:

            try:
                elements = self.driver.find_elements(
                    *locator
                )

                for element in elements:

                    if element.is_displayed():
                        return True

            except Exception:
                continue

        return False

    def is_cart_displayed(self):

        return (
            self.is_cart_content_visible()
            or
            "cart" in self.driver.current_url.lower()
        )

    def wait_for_cart(self):

        print("Waiting for cart...")

        try:
            self.wait.until(
                lambda driver:
                self.is_cart_displayed()
            )

            print("Cart displayed")

            return True

        except TimeoutException:

            print("Cart did not open automatically")

            return False

    def open_cart(self):

        if self.is_cart_displayed():

            print("Cart is already displayed")

            return True

        print("Opening cart manually...")

        try:
            self.safe_click(
                self.CART_ICON
            )

            self.wait.until(
                lambda driver:
                self.is_cart_displayed()
            )

            print("Cart opened")

            return True

        except TimeoutException:

            print("Cart could not be opened")

            return False

    # =========================================================
    # CART ITEM COUNT FOR EDGE TEST
    # =========================================================

    def get_cart_item_count(self):

        for locator in self.CART_ITEM_LOCATORS:

            try:
                elements = self.driver.find_elements(
                    *locator
                )

                visible_elements = [
                    element
                    for element in elements
                    if element.is_displayed()
                ]

                if visible_elements:
                    return len(visible_elements)

            except Exception:
                continue

        return 0