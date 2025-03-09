from tests.testbase import *
from config import BASE_URL, USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO


class TestShoppingCart:

    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.submitLoginForm(USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO)

        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.shopping_cart_button = self.shopping_cart_page.shopping_cart_button

        assert (
            self.driver.current_url == f"{BASE_URL}/inventory.html"
        ), "The redirection to the inventory page was not successful."
        assert (
            self.shopping_cart_button.is_displayed()
        ), "The shopping cart button is not present in the UI."

        yield self.driver

        wait = WebDriverWait(self.driver, 10)
        hamburger_menu_driver = wait.until(
            EC.element_to_be_clickable(
                self.shopping_cart_page.burger_menu_button_locator
            )
        )

        hamburger_menu_driver.click()
        log_out_button = wait.until(
            EC.element_to_be_clickable((self.shopping_cart_page.log_out_button))
        )
        log_out_button.click()

        self.driver.quit()

    def test_01_assert_browser_title(self, web: WebDriver):
        assert "Swag Labs" in web.title

    def test_02_add_to_cart(self, web: WebDriver):
        shopping_cart = ShoppingCartPage(web)

        product_name = shopping_cart.add_first_product_to_cart()
        shopping_cart.go_to_cart()

        assert "cart.html" in web.current_url, "Did not redirect to the cart page."
        assert (
            product_name == shopping_cart.get_first_product_name_in_cart()
        ), "The product in the cart does not match the added one."


if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
