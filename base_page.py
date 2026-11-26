# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 20)
#
#     def open_url(self, url):
#         self.driver.get(url)
#
#     def click(self, locator):
#         element = self.wait.until(
#             EC.element_to_be_clickable(locator)
#         )
#         element.click()
#
#     def enter_text(self, locator, text):
#         element = self.wait.until(
#             EC.visibility_of_element_located(locator)
#         )
#         element.clear()
#         element.send_keys(text)
#
#     def get_attribute(self, locator, attribute):
#         element = self.wait.until(
#             EC.visibility_of_element_located(locator)
#         )
#         return element.get_attribute(attribute)
#
#     def is_visible(self, locator):
#         try:
#             self.wait.until(
#                 EC.visibility_of_element_located(locator)
#             )
#             return True
#         except Exception:
#             return False

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            25,
            poll_frequency=0.5,
            ignored_exceptions=(
                StaleElementReferenceException,
            )
        )

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def find_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def safe_click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        try:
            element.click()

        except (
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )