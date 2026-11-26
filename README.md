Selenium Python Web Automation Framework
Project Overview

Developed an end-to-end web automation testing framework using Selenium WebDriver, Python, PyTest, and Page Object Model (POM). The framework automates major web application workflows and validates functionality through positive, negative, regression, and edge-case testing.

Technologies Used
Python
Selenium WebDriver
PyTest
Page Object Model (POM)
Git
GitHub
Key Features
Automated end-to-end web application workflows using Selenium WebDriver.
Developed reusable automation components using the Page Object Model.
Created structured and maintainable page objects with reusable locators and methods.
Implemented explicit waits for handling dynamic web elements.
Used PyTest assertions for validating expected application behavior.
Automated browser interactions, navigation, forms, field validations, product selection, cart, and checkout workflows.
Developed positive, negative, and edge-case test scenarios.
Supported functional and regression testing through reusable automated test scripts.
Maintained separation between page-level functionality and test-case logic.
Test Coverage

The automation framework covers:

Search functionality
Navigation and page validation
Filters and product selection
User registration
Input-field validations
Cart functionality
Checkout workflows
Positive scenarios
Negative scenarios
Edge-case scenarios
Regression scenarios
Framework Structure
Plain Text
project/
│
├── pages/
│ ├── home_page.py
│ ├── product_page.py
│ ├── register_page.py
│ └── checkout_page.py
│
├── tests/
│ ├── test_home.py
│ ├── test_product.py
│ ├── test_registration.py
│ └── test_checkout.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
How to Run the Tests

Install the required dependencies:

Shell
pip install selenium pytest

Run all test cases:

Shell
pytest -v

Run a specific test file:

Shell
pytest tests/test_home.py -v

Run regression tests using a configured PyTest marker:

Shell
pytest -m regression -v
Skills Demonstrated

Python | Selenium WebDriver | PyTest | Page Object Model | Web Automation | Functional Testing | Regression Testing | Positive Testing | Negative Testing | Edge-Case Testing | Locators | Explicit Waits | Assertions | Git | GitHub
