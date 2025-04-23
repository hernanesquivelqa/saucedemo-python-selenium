from tests.testbase import *
from config import (
    BASE_URL,
    USERNAME_SAUCEDEMO,
    PASSWORD_SAUCEDEMO,
    LOCKED_OUT_USER,
    INVALID_USERNAME,
)


class TestLogin:
    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        yield self.driver
        self.driver.quit()

    def test_verify_login_01(self, web: WebDriver):
        login_page = LoginPage(web)
        login_page.submit_login_form(USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO)
        shopping_cart_page = ShoppingCartInventoryPage(web)
        shopping_cart_page.click_burger_button()
        shopping_cart_page.log_out_button_click()
        assert BASE_URL == web.current_url[:-1]

    def test_locked_out_user_cannot_login(self, web: WebDriver):
        login_page = LoginPage(web)
        login_page.submit_login_form(LOCKED_OUT_USER, PASSWORD_SAUCEDEMO)
        error_message = login_page.error_message()
        expected_error_message = login_page.user_lockout_error_message
        assert error_message == expected_error_message, f"Expected: '{expected_error_message}', but got: '{error_message}'"
        assert BASE_URL == web.current_url[:-1]

    def test_invalid_username(self, web: WebDriver):
        login_page = LoginPage(web)
        login_page.submit_login_form(INVALID_USERNAME, PASSWORD_SAUCEDEMO)
        error_message = login_page.error_message()
        expected_error_message = login_page.invalid_username_error_message
        assert error_message == expected_error_message, f"Expected: '{expected_error_message}', but got: '{error_message}'"
        assert BASE_URL == web.current_url[:-1]
