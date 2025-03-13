from tests.testbase import *


class CartPage:
    def __init__(self, web: WebDriver):
        self.driver = web
        self.checkout_button = self.driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]')
        self.current_path = "https://www.saucedemo.com/cart.html"

    def checkout_button_click(self):
        self.checkout_button.click()
