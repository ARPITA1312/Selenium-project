import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    chrome_options = Options()

    prefs = {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    }

    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()