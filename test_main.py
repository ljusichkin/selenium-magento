import pytest
import allure
import time
from selenium.webdriver.common.by import By


@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Test Invalid Login')
@allure.description('Verifies that an invalid login attempt shows the correct error message.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_invalid_login(driver, config):
    with allure.step("Navigate to the login page"):
        driver.get(config["LOGIN_URL"])

    with allure.step("Enter invalid email"):
        user_email = driver.find_element(By.ID, "email")
        user_email.send_keys("invalidemail@gmail.com")

    with allure.step("Enter invalid password"):
        user_password = driver.find_element(By.ID, "pass")
        user_password.send_keys("invalidpassword")

    with allure.step("Click the login button"):
        submit_button = driver.find_element(By.ID, "send2")
        submit_button.click()

        time.sleep(3)

    with allure.step("Capture the error message displayed"):
        error_alert = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')

    with allure.step("Verify the error message text"):
        assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in error_alert.text, "Expected error message for invalid login was not displayed."


@allure.feature('User Authentication')
@allure.suite('Login Tests')
@allure.title('Test Valid Login')
@allure.description('Verifies that a valid login redirects to the account page.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver, config):
    with allure.step("Navigate to the login page"):
        driver.get(config["LOGIN_URL"])

    with allure.step("Enter valid email"):
        user_email = driver.find_element(By.ID, "email")
        user_email.send_keys(config["EMAIL"])

    with allure.step("Enter valid password"):
        user_password = driver.find_element(By.ID, "pass")
        user_password.send_keys(config["PASSWORD"])

    with allure.step("Click the login button"):
        submit_button = driver.find_element(By.ID, "send2")
        submit_button.click()

    time.sleep(3)

    with allure.step("Verify that the user is redirected to the account page"):
        assert driver.current_url == (config["ACCOUNT_URL"]), "User was not redirected to the account page after a successful login."


@allure.feature('User Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password with Incorrect Current Password')
@allure.description('Verifies that changing the password with an incorrect current password shows the correct error message.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_change_password_incorrect_current(driver, config):
    with allure.step("Navigate to the account page"):
        driver.get(config["ACCOUNT_URL"])

    with allure.step("Click on Change Password link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter incorrect current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(config["NEW_PASSWORD"])

    with allure.step("Confirm new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(config["NEW_PASSWORD"])

    with allure.step("Click the save button"):
        save_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
        save_button.click()

    time.sleep(3)
    with allure.step("Capture the error message displayed"):
        error_message = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')

    with allure.step("Verify the error message text"):
        assert "The password doesn't match this account. Verify the password and try again." in error_message.text, "Error message for incorrect current password was not displayed."


@allure.feature('User Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password with Mismatched Confirmation')
@allure.description('Verifies that changing the password with a mismatched confirmation shows the correct error message.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_change_password_mismatch(driver, config):
    with allure.step("Navigate to the account page"):
        driver.get(config["ACCOUNT_URL"])

    with allure.step("Click on Change Password link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(config["PASSWORD"])

    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(config["NEW_PASSWORD"])

    with allure.step("Enter mismatched confirmation password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")

    with allure.step("Click the save button"):
        save_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
        save_button.click()

    time.sleep(3)

    with allure.step("Capture the error message displayed"):
        error_message = driver.find_element(By.ID, "password-confirmation-error")

    with allure.step("Verify the error message text"):
        assert "Please enter the same value again." in error_message.text, "Error message for mismatched passwords was not displayed."


@allure.feature('User Account Management')
@allure.suite('Password Change Tests')
@allure.title('Test Change Password Successfully')
@allure.description('Verifies that changing the password successfully shows the correct success message.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_change_password(driver, config):
    with allure.step("Navigate to the account page"):
        driver.get(config["ACCOUNT_URL"])

    with allure.step("Click on Change Password link"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(config["PASSWORD"])

    with allure.step("Enter new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(config["NEW_PASSWORD"])

    with allure.step("Confirm new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(config["NEW_PASSWORD"])

    with allure.step("Click the save button"):
        save_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
        save_button.click()

    with allure.step("Capture the success message displayed"):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")

    with allure.step("Verify the success message text"):
        assert 'You saved the account information.' in success_message.text, "The success message was not displayed as expected."





