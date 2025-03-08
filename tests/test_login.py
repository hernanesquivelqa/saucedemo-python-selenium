from tests.testbase import *
from config import BASE_URL, USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO, LOCKED_OUT_USER
import time


class TestLogin:
    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        yield self.driver
        self.driver.quit()

    def test_verify_login_01(self, web: WebDriver):
        login_page = LoginPage(web)
        login_page.submitLoginForm(USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO)
        shopping_cart_page = ShoppingCartPage(web)
        burger_menu = shopping_cart_page.burger_menu_button
        burger_menu.click()
        log_out_button = shopping_cart_page.log_out
        web.implicitly_wait(10)
        log_out_button.click()
        assert BASE_URL == web.current_url[:-1]

    def test_locked_out_user_cannot_login(self, web: WebDriver):
        login_page = LoginPage(web)
        login_page.submitLoginForm(LOCKED_OUT_USER, PASSWORD_SAUCEDEMO)
        error_message = login_page.error_message_look_out()
        correct_error_message = login_page.user_look_out_error_message
        assert (
            error_message == correct_error_message
        ), f"Expected: '{correct_error_message}', but got: '{error_message}'"
        assert BASE_URL == web.current_url[:-1]
