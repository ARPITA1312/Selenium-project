from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    InvalidSessionIdException
)

from pages.base_page import BasePage


class RegisterPage(BasePage):

    URL = "https://www.lenskart.com/"

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
        "//*[contains("
        "translate(normalize-space(.),"
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
        "'abcdefghijklmnopqrstuvwxyz'),"
        "'sign in or register')]"
    )

    CREATE_ACCOUNT_LINK = (
        By.XPATH,
        '//*[@id="sign-in-form"]/div/div[2]/div[5]/button'
    )

    # =========================================================
    # REGISTRATION FORM LOCATORS
    # =========================================================

    FIRST_NAME_INPUT = (
        By.XPATH,
        '//*[@id="sign-up-form"]/div/div[2]/div[1]/div[1]/input'
    )

    LAST_NAME_INPUT = (
        By.XPATH,
        '//*[@id="sign-up-form"]/div/div[2]/div[2]/div[1]/input'
    )

    MOBILE_INPUT = (
        By.XPATH,
        '//*[@id="sign-up-form"]/div/div[2]/div[3]/div[1]/input'
    )

    EMAIL_INPUT = (
        By.XPATH,
        '//*[@id="sign-up-form"]/div/div[2]/div[4]/div[1]/input'
    )

    PASSWORD_INPUT = (
        By.XPATH,
        '//*[@id="sign-up-form"]/div/div[2]/div[5]/div[1]/input'
    )

    CREATE_ACCOUNT_BUTTON = (
        By.ID,
        "remove-button"
    )

    # =========================================================
    # COMMON WAIT
    # =========================================================

    def get_wait(self, timeout=25):

        return WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=0.5,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

    # =========================================================
    # STEP 1: OPEN HOMEPAGE
    # =========================================================

    def open_homepage(self):

        print("Opening Lenskart homepage...")

        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.get_wait(25).until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        print("Lenskart homepage displayed")

    def is_homepage_displayed(self):

        try:
            return (
                "lenskart.com"
                in self.driver.current_url.lower()
            )

        except InvalidSessionIdException:
            return False

    # =========================================================
    # STEP 2: CLICK ACCOUNT ICON
    # =========================================================

    def click_account_icon(self):

        print("Waiting for Account icon...")

        wait = self.get_wait(30)

        account_icon = wait.until(
            EC.presence_of_element_located(
                self.ACCOUNT_ICON
            )
        )

        print("Account icon found")

        account_icon = wait.until(
            EC.visibility_of_element_located(
                self.ACCOUNT_ICON
            )
        )

        print("Account icon visible")

        try:

            account_icon = wait.until(
                EC.element_to_be_clickable(
                    self.ACCOUNT_ICON
                )
            )

            account_icon.click()

            print("Account icon clicked normally")

        except (
            TimeoutException,
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):

            print(
                "Normal click failed. "
                "Using JavaScript click."
            )

            account_icon = wait.until(
                EC.presence_of_element_located(
                    self.ACCOUNT_ICON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                account_icon
            )

            print(
                "Account icon clicked using JavaScript"
            )

    # =========================================================
    # STEP 3: CLICK SIGN IN / REGISTER
    # =========================================================

    def click_sign_in_register(self):

        print("Waiting for Sign In/Register...")

        try:

            account_menu = self.get_wait(8).until(
                EC.presence_of_element_located(
                    self.ACCOUNT_MENU
                )
            )

            print("Account menu found")

            try:
                account_menu.click()

            except Exception:

                self.driver.execute_script(
                    "arguments[0].click();",
                    account_menu
                )

            print("Account menu clicked")

        except TimeoutException:

            print(
                "Account menu not found. "
                "Trying Sign In/Register text."
            )

            option = self.get_wait(20).until(
                EC.presence_of_element_located(
                    self.SIGN_IN_REGISTER
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                option
            )

            print("Sign In/Register clicked")

    # =========================================================
    # STEP 4: VERIFY CREATE ACCOUNT
    # =========================================================

    def is_create_account_displayed(self):

        try:

            button = self.get_wait(20).until(
                EC.visibility_of_element_located(
                    self.CREATE_ACCOUNT_LINK
                )
            )

            return button.is_displayed()

        except (
            TimeoutException,
            InvalidSessionIdException
        ):

            return False

    # =========================================================
    # STEP 5: CLICK CREATE ACCOUNT
    # =========================================================

    def click_create_account(self):

        print("Waiting for Create an Account...")

        wait = self.get_wait(20)

        button = wait.until(
            EC.presence_of_element_located(
                self.CREATE_ACCOUNT_LINK
            )
        )

        button = wait.until(
            EC.element_to_be_clickable(
                self.CREATE_ACCOUNT_LINK
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
                    self.CREATE_ACCOUNT_LINK
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                button
            )

        print("Create an Account clicked")

    # =========================================================
    # CHECK BROWSER SESSION
    # =========================================================

    def is_browser_session_active(self):

        try:

            _ = self.driver.current_url
            _ = self.driver.title

            return True

        except InvalidSessionIdException:

            return False

    # =========================================================
    # STEP 6: VERIFY REGISTRATION FORM
    # =========================================================

    def is_registration_form_displayed(self):

        print("Checking Registration form...")

        try:

            fields = self.get_wait(20).until(
                lambda driver:
                driver.find_elements(
                    *self.FIRST_NAME_INPUT
                )
            )

            print(
                f"First Name elements found: {len(fields)}"
            )

            for field in fields:

                if field.is_displayed():

                    print(
                        "Registration form displayed"
                    )

                    return True

            return False

        except (
            TimeoutException,
            InvalidSessionIdException
        ):

            return False

    # =========================================================
    # REUSABLE INPUT METHOD
    # =========================================================

    def enter_registration_value(
            self,
            locator,
            value,
            field_name
    ):

        print(
            f"Waiting for {field_name}..."
        )

        wait = self.get_wait(20)

        field = wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            field
        )

        field = wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        try:

            field.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                field
            )

        field.clear()
        field.send_keys(value)

        print(
            f"{field_name} entered"
        )

    # =========================================================
    # FIELD METHODS
    # =========================================================

    def enter_first_name(self, first_name):

        self.enter_registration_value(
            self.FIRST_NAME_INPUT,
            first_name,
            "First Name"
        )

    def enter_last_name(self, last_name):

        self.enter_registration_value(
            self.LAST_NAME_INPUT,
            last_name,
            "Last Name"
        )

    def enter_mobile(self, mobile):

        self.enter_registration_value(
            self.MOBILE_INPUT,
            mobile,
            "Mobile Number"
        )

    def enter_email(self, email):

        self.enter_registration_value(
            self.EMAIL_INPUT,
            email,
            "Email"
        )

    def enter_password(self, password):

        self.enter_registration_value(
            self.PASSWORD_INPUT,
            password,
            "Password"
        )

    # =========================================================
    # FILL COMPLETE FORM
    # =========================================================

    def fill_registration_form(
            self,
            first_name,
            last_name,
            mobile,
            email,
            password
    ):

        print(
            "Entering registration details..."
        )

        self.enter_first_name(
            first_name
        )

        self.enter_last_name(
            last_name
        )

        self.enter_mobile(
            mobile
        )

        self.enter_email(
            email
        )

        self.enter_password(
            password
        )

        print(
            "All registration details entered successfully"
        )

    # =========================================================
    # VERIFY VALUES
    # =========================================================

    def is_registration_information_entered(self):

        fields = [
            self.FIRST_NAME_INPUT,
            self.LAST_NAME_INPUT,
            self.MOBILE_INPUT,
            self.EMAIL_INPUT,
            self.PASSWORD_INPUT
        ]

        for locator in fields:

            try:

                field = self.get_wait(10).until(
                    EC.visibility_of_element_located(
                        locator
                    )
                )

                value = field.get_attribute(
                    "value"
                )

                if not value:
                    return False

            except (
                TimeoutException,
                InvalidSessionIdException
            ):

                return False

        return True

    # =========================================================
    # SUBMIT CREATE ACCOUNT
    # =========================================================

    def submit_create_account(self):

        print(
            "Waiting for Create Account button..."
        )

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

        print(
            "Create Account button clicked"
        )