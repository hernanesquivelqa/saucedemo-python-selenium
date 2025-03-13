from config import *
from tests.testbase import *


class CheckOutCompletePage:
    def __init__(self, web: WebDriver):
        self.driver = web
        self.pathUrl = "/checkout-complete.html"
        self.confirmation_messages = {"confirmation": "Thank you for your order!", "order_dispatched": "Your order has been dispatched, and will arrive just as fast as the pony can get there!"}
        self.order_confirmation = self.driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]')
        self.order_dispatched = self.driver.find_element(By.CSS_SELECTOR, '[data-test="complete-text"]')
        self.back_to_home_page_button = self.driver.find_element(By.CSS_SELECTOR, '[data-test="back-to-products"]')

    def text_order_confirmation(self):
        return self.order_confirmation.text

    def text_order_dispatched(self):
        return self.order_dispatched.text

    def back_to_home_page(self):
        self.back_to_home_page_button.click()
