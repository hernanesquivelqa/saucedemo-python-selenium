from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.testbase import *
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.web = driver
        self.locators  = Locators(driver)
        self.username_input = lambda: self.locators.by_data_test("username")
        self.password_input = lambda: self.locators.by_data_test("password")
        self.submit_button = lambda: self.locators.by_data_test("login-button")
        self.message_error_locator = (
            By.CLASS_NAME,
            "error-message-container",
        )
        self.problem_user_message_error_locator = ()

        #
        # ERROR MESSAGES
        #
        self.user_lockout_error_message = "Epic sadface: Sorry, this user has been locked out."
        self.invalid_username_error_message = "Epic sadface: Username and password do not match any user in this service"

    def enter_username(self, input_value: str):
        return self.username_input().send_keys(input_value)

    def enter_password(self, input_value: str):
        return self.password_input().send_keys(input_value)

    def click_submit(self):
        return self.submit_button().click()

    def submit_login_form(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def error_message(self):
        return self.web.find_element(*self.message_error_locator).text
