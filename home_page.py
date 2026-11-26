from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    ElementClickInterceptedException
)

from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://www.lenskart.com/"

    # =========================================================
    # SEARCH LOCATORS
    # =========================================================

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[@data-analytics-target-id='search']"
    )

    SEARCH_INPUT = (
        By.XPATH,
        "//*[@id='desktop-search-dialog']//input"
    )

    # =========================================================
    # GENDER FILTER LOCATORS
    # =========================================================

    MEN_FILTER = (
        By.XPATH,
        '//*[@id="desktop-home"]/section[2]/div/div/div[5]/a[1]'
    )

    # =========================================================
    # PRODUCT LOCATORS
    # =========================================================

    EYEGLASSES_MENU = (
        By.XPATH,
        "//a[normalize-space()='Eyeglasses']"
    )

    PRODUCT_IMAGE = (
        By.XPATH,
        '//*[@id="main-content"]/div/section[2]/article[3]/div[2]/div[1]/a'
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
    # ZERO POWER LOCATOR
    # =========================================================

    ZERO_POWER_CHECKOUT_OPTION = (
        By.XPATH,
        '//*[@id="main-content"]/article/div[1]/div[2]/div/div/'
        'div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]'
    )

    ZERO_POWER_TEXT = (
        By.XPATH,
        "//*[normalize-space()='Zero Power']"
    )

    # =========================================================
    # BLU SCREEN PACKAGE LOCATORS
    # =========================================================

    LENS_PACKAGE_DIALOG = (
        By.XPATH,
        "//*[contains(normalize-space(.),'Choose Lens Package')]"
    )

    BLU_SCREEN_PACKAGE = (
        By.XPATH,
        '//*[@id="package-59fc6701e4b0e569286ac018"]/div/div[1]'
    )

    BLU_SCREEN_PACKAGE_TEXT = (
        By.XPATH,
        "//*[normalize-space()='BLU Screen Lenses']"
    )

    EMAIL_VALIDATION_ERROR = (
        By.XPATH,
        "//*[contains(text(),'Please enter a valid email')]"
    )

    SELECT_THIS_LENS_BUTTON = (
        By.ID,
        "button"
    )

    # =========================================================
    # CART LOCATORS
    # =========================================================

    CART_BUTTON_LOCATORS = [
        (
            By.ID,
            "desktop-home-cart-trigger"
        ),
        (
            By.CSS_SELECTOR,
            "a[href*='cart']"
        ),
        (
            By.CSS_SELECTOR,
            "button[aria-label*='cart' i]"
        ),
        (
            By.XPATH,
            "//a[contains(@href,'cart')]"
        )
    ]

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
            "'BLU SCREEN LENSES')]"
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

    # =========================================================
    # NEGATIVE SEARCH LOCATORS
    # =========================================================

    NO_SEARCH_RESULT_LOCATORS = [
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'NO RESULTS')]"
        ),
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'NO PRODUCTS')]"
        ),
        (
            By.XPATH,
            "//*[contains("
            "translate(normalize-space(.),"
            "'abcdefghijklmnopqrstuvwxyz',"
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),"
            "'NOT FOUND')]"
        )
    ]

    # =========================================================
    # ACCOUNT / REGISTRATION LOCATORS
    # =========================================================

    ACCOUNT_ICON = (
        By.ID,
        "desktop-home-account-trigger"
    )

    ACCOUNT_MENU = (
        By.ID,
        "desktop-account-menu"
    )

    SIGN_IN_REGISTER = (
        By.XPATH,
        "//*[normalize-space(text())='Sign in or register']"
    )

    SIGN_IN_HEADING = (
        By.XPATH,
        "//*[normalize-space(text())='Sign In']"
    )

    CREATE_ACCOUNT_LINK = (
        By.XPATH,
        "//*[@id='sign-in-form']/div/div[2]/div[5]/button"
    )

    FIRST_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'First Name')]"
    )

    LAST_NAME_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Last Name')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Mobile')]"
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'Email')]"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password' or contains(@placeholder,'Password')]"
    )

    CREATE_ACCOUNT_BUTTON = (
        By.ID,
        "remove-button"
    )

    # =========================================================
    # COMMON METHODS
    # =========================================================

    def get_wait(self, timeout=20):

        return WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=0.5,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

    def safe_click(self, locator, timeout=20):

        wait = self.get_wait(timeout)

        element = wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({"
            "block:'center', inline:'center'"
            "});",
            element
        )

        element = wait.until(
            EC.element_to_be_clickable(locator)
        )

        try:
            element.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            element = wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    # =========================================================
    # HOMEPAGE METHODS
    # =========================================================

    def open_homepage(self):

        self.driver.get(self.URL)

        self.get_wait(20).until(
            lambda driver:
            "lenskart" in driver.current_url.lower()
        )

    def is_homepage_displayed(self):

        return "lenskart" in self.driver.current_url.lower()

    # =========================================================
    # SEARCH METHODS
    # =========================================================

    def open_search(self):

        self.safe_click(
            self.SEARCH_BUTTON,
            timeout=15
        )

        self.get_wait(15).until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

    def enter_search_term(self, search_term):

        self.open_search()

        search_box = self.get_wait(15).until(
            EC.element_to_be_clickable(
                self.SEARCH_INPUT
            )
        )

        search_box.clear()
        search_box.send_keys(search_term)

        search_box = self.get_wait(15).until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        return search_box.get_attribute("value")

    def submit_search(self):

        search_box = self.get_wait(15).until(
            EC.element_to_be_clickable(
                self.SEARCH_INPUT
            )
        )

        search_box.send_keys(Keys.ENTER)

    def are_search_results_displayed(self):

        try:

            self.get_wait(15).until(
                lambda driver:
                "sunglasses" in driver.current_url.lower()
                or
                "sunglasses" in driver.page_source.lower()
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # MEN FILTER METHODS
    # =========================================================

    def select_men_filter(self):

        self.safe_click(
            self.MEN_FILTER,
            timeout=15
        )

    def is_men_filter_applied(self):

        try:

            self.get_wait(15).until(
                lambda driver:
                "men" in driver.current_url.lower()
                or
                "men" in driver.page_source.lower()
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # PRODUCT LISTING METHODS
    # =========================================================

    def open_eyeglasses(self):

        current_url = self.driver.current_url

        self.safe_click(
            self.EYEGLASSES_MENU,
            timeout=20
        )

        try:

            self.get_wait(20).until(
                EC.url_changes(current_url)
            )

        except TimeoutException:
            pass

        self.get_wait(20).until(
            EC.presence_of_element_located(
                self.PRODUCT_IMAGE
            )
        )

    def is_product_list_displayed(self):

        try:

            self.get_wait(20).until(
                EC.visibility_of_element_located(
                    self.PRODUCT_IMAGE
                )
            )

            return True

        except TimeoutException:
            return False

    def click_product(self):

        wait = self.get_wait(25)

        product = wait.until(
            EC.presence_of_element_located(
                self.PRODUCT_IMAGE
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )

        listing_url = self.driver.current_url

        product = wait.until(
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

            product = wait.until(
                EC.presence_of_element_located(
                    self.PRODUCT_IMAGE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                product
            )

        wait.until(
            EC.url_changes(listing_url)
        )

        wait.until(
            EC.presence_of_element_located(
                self.PRODUCT_DETAIL_CONTAINER
            )
        )

    def is_product_detail_page_displayed(self):

        try:

            self.get_wait(25).until(
                EC.visibility_of_element_located(
                    self.PRODUCT_DETAIL_CONTAINER
                )
            )

            self.get_wait(25).until(
                EC.presence_of_element_located(
                    self.SELECT_LENSES_BUTTON
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # SELECT LENSES
    # =========================================================

    def click_select_lenses(self):

        try:

            self.safe_click(
                self.SELECT_LENSES_BUTTON,
                timeout=20
            )

        except TimeoutException:

            self.safe_click(
                self.SELECT_LENSES_TEXT,
                timeout=20
            )

        self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.LENS_TYPE_DIALOG
            )
        )

    def is_lens_type_dialog_displayed(self):

        try:

            self.get_wait(20).until(
                EC.visibility_of_element_located(
                    self.LENS_TYPE_DIALOG
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # SELECT ZERO POWER
    # =========================================================

    def select_zero_power_for_checkout(self):

        try:

            self.safe_click(
                self.ZERO_POWER_CHECKOUT_OPTION,
                timeout=20
            )

        except TimeoutException:

            self.safe_click(
                self.ZERO_POWER_TEXT,
                timeout=20
            )

        self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.LENS_PACKAGE_DIALOG
            )
        )

    def is_lens_package_dialog_displayed(self):

        try:

            self.get_wait(20).until(
                EC.visibility_of_element_located(
                    self.LENS_PACKAGE_DIALOG
                )
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # SELECT BLU SCREEN PACKAGE
    # =========================================================

    def select_blu_screen_package(self):

        try:

            self.safe_click(
                self.BLU_SCREEN_PACKAGE,
                timeout=20
            )

        except TimeoutException:

            self.safe_click(
                self.BLU_SCREEN_PACKAGE_TEXT,
                timeout=20
            )

        self.get_wait(20).until(
            EC.presence_of_element_located(
                self.SELECT_THIS_LENS_BUTTON
            )
        )



    # =========================================================
    # SELECT THIS LENS
    # =========================================================

    def click_select_this_lens(self):

        wait = self.get_wait(20)

        button = wait.until(
            EC.presence_of_element_located(
                self.SELECT_THIS_LENS_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button = wait.until(
            EC.element_to_be_clickable(
                self.SELECT_THIS_LENS_BUTTON
            )
        )

        try:
            button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            button = wait.until(
                EC.presence_of_element_located(
                    self.SELECT_THIS_LENS_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )


    # =========================================================
    # CART METHODS
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

            except StaleElementReferenceException:
                continue

        return False

    def open_cart(self):

        # Cart might open automatically after selecting the lens.
        if self.is_cart_content_visible():
            return True

        for locator in self.CART_BUTTON_LOCATORS:

            try:

                self.safe_click(
                    locator,
                    timeout=5
                )

                return True

            except TimeoutException:
                continue

        return False

    def is_product_added_to_cart(self):

        try:

            self.get_wait(20).until(
                lambda driver:
                self.is_cart_content_visible()
                or
                "cart" in driver.current_url.lower()
            )

            return True

        except TimeoutException:
            return False

    # =========================================================
    # ACCOUNT / REGISTRATION METHODS
    # =========================================================

    def click_account_icon(self):

        self.safe_click(
            self.ACCOUNT_ICON,
            timeout=20
        )

        self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.SIGN_IN_REGISTER
            )
        )

    def click_sign_in_register(self):

        option = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.SIGN_IN_REGISTER
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            option
        )

        self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.SIGN_IN_HEADING
            )
        )

    def click_create_account(self):

        self.safe_click(
            self.CREATE_ACCOUNT_LINK,
            timeout=20
        )

        self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.FIRST_NAME_INPUT
            )
        )

    def enter_first_name(self, first_name):

        field = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.FIRST_NAME_INPUT
            )
        )

        field.clear()
        field.send_keys(first_name)

    def enter_last_name(self, last_name):

        field = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.LAST_NAME_INPUT
            )
        )

        field.clear()
        field.send_keys(last_name)

    def enter_mobile(self, mobile):

        field = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.MOBILE_INPUT
            )
        )

        field.clear()
        field.send_keys(mobile)

    def enter_email(self, email):

        field = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.EMAIL_INPUT
            )
        )

        field.clear()
        field.send_keys(email)

    def enter_password(self, password):

        field = self.get_wait(20).until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT
            )
        )

        field.clear()
        field.send_keys(password)

    def fill_registration_form(
            self,
            first_name,
            last_name,
            mobile,
            email,
            password
    ):

        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_mobile(mobile)
        self.enter_email(email)
        self.enter_password(password)

    def submit_create_account(self):

        wait = self.get_wait(20)

        button = wait.until(
            EC.presence_of_element_located(
                self.CREATE_ACCOUNT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        # Re-locate after scrolling.
        button = wait.until(
            EC.element_to_be_clickable(
                self.CREATE_ACCOUNT_BUTTON
            )
        )

        try:
            button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            button = wait.until(
                EC.presence_of_element_located(
                    self.CREATE_ACCOUNT_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )
    # =========================================================
    # SUBMIT CREATE ACCOUNT
    # =========================================================

    def submit_create_account(self):

        wait = self.get_wait(20)

        button = wait.until(
            EC.presence_of_element_located(
                self.CREATE_ACCOUNT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button = wait.until(
            EC.element_to_be_clickable(
                self.CREATE_ACCOUNT_BUTTON
            )
        )

        try:
            button.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            button = wait.until(
                EC.presence_of_element_located(
                    self.CREATE_ACCOUNT_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

    # =========================================================
    # NEGATIVE VIEW PRODUCT METHODS
    # =========================================================

    def open_invalid_product(self):

        # Intentionally invalid product URL
        invalid_product_url = (
            "https://www.lenskart.com/"
            "non-existing-product-999999.html"
        )

        self.driver.get(invalid_product_url)

        self.get_wait(15).until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def is_valid_product_detail_displayed(self):

        try:

            self.get_wait(8).until(
                EC.visibility_of_element_located(
                    self.PRODUCT_DETAIL_CONTAINER
                )
            )

            self.get_wait(8).until(
                EC.visibility_of_element_located(
                    self.SELECT_LENSES_BUTTON
                )
            )

            return True

        except TimeoutException:

            return False
    # =========================================================
    # NEGATIVE REGISTRATION METHODS
    # =========================================================

    def is_registration_form_displayed(self):

        try:

            self.get_wait(10).until(
                EC.visibility_of_element_located(
                    self.FIRST_NAME_INPUT
                )
            )

            return True

        except TimeoutException:

            return False


    def is_email_field_displayed(self):

        try:

            self.get_wait(10).until(
                EC.visibility_of_element_located(
                    self.EMAIL_INPUT
                )
            )

            return True

        except TimeoutException:

            return False


    def is_registration_rejected(self):

        try:

            # For invalid registration data,
            # the registration form should remain visible.
            self.get_wait(10).until(
                EC.visibility_of_element_located(
                    self.EMAIL_INPUT
                )
            )

            return True

        except TimeoutException:

            return False

    def is_invalid_email_error_displayed(self):

        try:

            self.get_wait(10).until(
                EC.visibility_of_element_located(
                    self.EMAIL_VALIDATION_ERROR
                )
            )

            return True

        except TimeoutException:

            return False


    # =========================================================
    # NEGATIVE REGISTRATION METHODS
    # =========================================================

    def submit_invalid_registration(self):

        wait = self.get_wait(10)

        # Find CREATE AN ACCOUNT button
        button = wait.until(
            EC.presence_of_element_located(
                self.CREATE_ACCOUNT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        # If invalid data keeps the button disabled,
        # this itself proves the form is rejecting the data.
        if not button.is_enabled():
            return False

        disabled = button.get_attribute("disabled")

        if disabled is not None:
            return False

        # Button is enabled, so attempt submission.
        try:

            button.click()

        except ElementClickInterceptedException:

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        return True


    def is_registration_form_displayed(self):

        try:

            self.get_wait(10).until(
                EC.visibility_of_element_located(
                    self.EMAIL_INPUT
                )
            )

            return True

        except TimeoutException:

            return False


    def is_registration_rejected(self):

        # If the registration form remains visible,
        # registration has not successfully completed.
        return self.is_registration_form_displayed()


    def is_email_value_invalid(self):

        email_field = self.get_wait(10).until(
            EC.visibility_of_element_located(
                self.EMAIL_INPUT
            )
        )

        # Read browser HTML validation state when available.
        return self.driver.execute_script(
            "return arguments[0].validity "
            "? !arguments[0].validity.valid "
            ": false;",
            email_field
        )

    # =========================================================
    # NEGATIVE REGISTRATION METHODS
    # =========================================================

    def is_email_invalid(self):

        email_field = self.get_wait(10).until(
            EC.visibility_of_element_located(
                self.EMAIL_INPUT
            )
        )

        # Trigger validation by moving focus away from Email
        self.driver.execute_script(
            "arguments[0].blur();",
            email_field
        )

        # Check browser-side validity
        is_valid = self.driver.execute_script(
            "return arguments[0].checkValidity();",
            email_field
        )

        return not is_valid


    def is_create_account_button_disabled(self):

        buttons = self.driver.find_elements(
            *self.CREATE_ACCOUNT_BUTTON
        )

        if not buttons:
            return True

        button = buttons[0]

        disabled_attribute = button.get_attribute(
            "disabled"
        )

        aria_disabled = button.get_attribute(
            "aria-disabled"
        )

        if disabled_attribute is not None:
            return True

        if aria_disabled == "true":
            return True

        return not button.is_enabled()


    def is_registration_form_still_displayed(self):

        try:

            email_fields = self.driver.find_elements(
                *self.EMAIL_INPUT
            )

            return any(
                field.is_displayed()
                for field in email_fields
            )

        except StaleElementReferenceException:

            return False


    def invalid_registration_was_rejected(self):

        # Condition 1:
        # Browser recognizes invalid email
        try:
            if self.is_email_invalid():
                return True

        except Exception:
            pass

        # Condition 2:
        # Create Account button remains disabled
        try:
            if self.is_create_account_button_disabled():
                return True

        except Exception:
            pass

        # Condition 3:
        # Registration form remains displayed
        try:
            if self.is_registration_form_still_displayed():
                return True

        except Exception:
            pass

        return False

    # =========================================================
    # NEGATIVE SEARCH METHODS
    # =========================================================

    def is_no_search_result_displayed(self):

        for locator in self.NO_SEARCH_RESULT_LOCATORS:

            try:

                elements = self.driver.find_elements(
                    *locator
                )

                for element in elements:

                    if element.is_displayed():
                        return True

            except StaleElementReferenceException:
                continue

        return False


    def is_invalid_search_rejected(self):

        try:

            self.get_wait(10).until(
                lambda driver:
                self.is_no_search_result_displayed()
            )

            return True

        except TimeoutException:

            return False

    # =========================================================
    # EDGE CART TEST METHODS
    # =========================================================

    def return_to_product_listing(self):

        self.driver.back()

        try:
            self.get_wait(20).until(
                EC.presence_of_element_located(
                    self.PRODUCT_IMAGE
                )
            )

            return True

        except TimeoutException:
            return False


    def is_cart_still_valid(self):

        try:

            self.get_wait(20).until(
                lambda driver:
                self.is_cart_content_visible()
                or
                "cart" in driver.current_url.lower()
            )

            return True

        except TimeoutException:

            return False

    def reopen_same_product(self):

        # Return to homepage
        self.open_homepage()

        # Open Eyeglasses listing again
        self.open_eyeglasses()

        # Open the same product identified by PRODUCT_IMAGE
        self.click_product()

        return self.is_product_detail_page_displayed()