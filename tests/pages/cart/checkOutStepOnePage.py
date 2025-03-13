from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.locators import Locators
from tests.testbase import *


class CheckOutStepOnePage:
    def __init__(self, web: WebDriver):
        self.driver = web
        self.get = Locators(self.driver)
        self.firstName = lambda: self.get.by_data_test("firstName")
        self.lastName = lambda: self.get.by_data_test("lastName")
        self.postCode = lambda: self.get.by_data_test("postalCode")
        self.buttonContinue = lambda: self.get.by_data_test("continue")

    def fill_out_form_and_continue(self, first_name: str, last_name: str, postal_code: str):
        self.firstName().send_keys(first_name)
        self.lastName().send_keys(last_name)
        self.postCode().send_keys(postal_code)
        self.buttonContinue().click()
