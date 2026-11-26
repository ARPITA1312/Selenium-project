import pytest

from pages.register_page import RegisterPage


@pytest.mark.register
def test_register_new_user(driver):

    register_page = RegisterPage(driver)

    # =========================================================
    # STEP 1: OPEN LENSKART HOMEPAGE
    # =========================================================

    print("\nSTEP 1: Open Lenskart homepage")

    register_page.open_homepage()

    assert register_page.is_homepage_displayed(), (
        "Lenskart homepage was not displayed."
    )

    print("STEP 1 PASSED")

    # =========================================================
    # STEP 2: CLICK ACCOUNT ICON
    # =========================================================

    print("STEP 2: Click Account icon")

    register_page.click_account_icon()

    print("STEP 2 PASSED")

    # =========================================================
    # STEP 3: CLICK SIGN IN / REGISTER
    # =========================================================

    print("STEP 3: Click Sign In/Register")

    register_page.click_sign_in_register()

    print("STEP 3 PASSED")

    # =========================================================
    # STEP 4: VERIFY CREATE ACCOUNT OPTION
    # =========================================================

    print("STEP 4: Verify Create Account option")

    assert register_page.is_create_account_displayed(), (
        "Create Account option was not displayed."
    )

    print("STEP 4 PASSED")

    # =========================================================
    # STEP 5: CLICK CREATE ACCOUNT
    # =========================================================

    print("STEP 5: Click Create Account")

    register_page.click_create_account()

    print("STEP 5 PASSED")

    # =========================================================
    # STEP 6: VERIFY BROWSER SESSION
    # =========================================================

    print("STEP 6: Verify browser session")

    assert register_page.is_browser_session_active(), (
        "Chrome/WebDriver session disconnected "
        "after clicking Create Account."
    )

    print("STEP 6 PASSED")

    # =========================================================
    # STEP 7: VERIFY REGISTRATION FORM
    # =========================================================

    print("STEP 7: Verify Registration form")

    assert register_page.is_registration_form_displayed(), (
        "Registration form was not displayed."
    )

    print("STEP 7 PASSED")

    # =========================================================
    # STEP 8: ENTER FIRST NAME
    # =========================================================

    print("STEP 8: Enter First Name")

    register_page.enter_first_name(
        "Test"
    )

    print("STEP 8 PASSED")

    # =========================================================
    # STEP 9: ENTER LAST NAME
    # =========================================================

    print("STEP 9: Enter Last Name")

    register_page.enter_last_name(
        "User"
    )

    print("STEP 9 PASSED")

    # =========================================================
    # STEP 10: ENTER MOBILE NUMBER
    # =========================================================

    print("STEP 10: Enter Mobile Number")

    register_page.enter_mobile(
        "9087654321"
    )

    print("STEP 10 PASSED")

    # =========================================================
    # STEP 11: ENTER EMAIL
    # =========================================================

    print("STEP 11: Enter Email")

    register_page.enter_email(
        "arpita.lenskart@gmail.com"
    )

    print("STEP 11 PASSED")

    # =========================================================
    # STEP 12: ENTER PASSWORD
    # =========================================================

    print("STEP 12: Enter Password")

    register_page.enter_password(
        "Test@12345"
    )

    print("STEP 12 PASSED")

    # =========================================================
    # STEP 13: VERIFY ALL REGISTRATION DETAILS
    # =========================================================

    print("STEP 13: Verify Registration details")

    assert (
        register_page.is_registration_information_entered()
    ), (
        "One or more registration fields "
        "were not populated correctly."
    )

    print("STEP 13 PASSED")

    # =========================================================
    # STEP 14: SUBMIT CREATE ACCOUNT
    # =========================================================

    print("STEP 14: Click Create Account")

    register_page.submit_create_account()

    print("STEP 14 PASSED")

    # =========================================================
    # TEST COMPLETED
    # =========================================================

    print(
        "\nREGISTRATION TEST COMPLETED SUCCESSFULLY"
    )