from tests.testbase import *
from config import BASE_URL, USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO, USERNAME_DEMOQA, LASTNAME_SAUCEDEMO, POSTAL_CODE_SAUCEDEMO


class TestShoppingCart:

    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.submit_login_form(USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO)
        self.inventory_page = ShoppingCartInventoryPage(self.driver)
        yield self.driver
        self.inventory_page.click_burger_button()
        self.inventory_page.log_out_button_click()
        self.driver.quit()

    def test_01_assert_browser_title(self, web: WebDriver):
        assert "Swag Labs" in web.title

    def test_02_add_to_cart(self, web: WebDriver):
        inventory_page = ShoppingCartInventoryPage(web)
        product_name = inventory_page.add_first_product_to_cart()
        inventory_page.go_to_cart()
        assert "cart.html" in web.current_url
        assert product_name == inventory_page.get_first_product_name_in_cart(), inventory_page.error_messages["not_match"]

    def test_03_checkout_one_item(self, web: WebDriver):
        inventory_page = ShoppingCartInventoryPage(web)
        product_name = inventory_page.add_first_product_to_cart()

        inventory_page.go_to_cart()
        # Cart Page
        cart_page = CartPage(web)
        assert cart_page.current_path == web.current_url
        assert product_name == inventory_page.get_first_product_name_in_cart(), inventory_page.error_messages["not_match"]
        cart_page.checkout_button_click()

        # Checkout Step One
        assert "checkout-step-one.html" in web.current_url
        checkOutStepOnePage = CheckOutStepOnePage(web)
        checkOutStepOnePage.fill_out_form_and_continue(USERNAME_DEMOQA, LASTNAME_SAUCEDEMO, POSTAL_CODE_SAUCEDEMO)
        # Checkout Step Two
        assert "checkout-step-two.html" in web.current_url
        self.driver.find_element(By.ID, "finish").click()
        # Checkout Complete
        confirmation_page = CheckOutCompletePage(web)
        order_confirmation = confirmation_page.text_order_confirmation()
        order_dispatched = confirmation_page.text_order_dispatched()

        assert order_confirmation == confirmation_page.confirmation_messages["confirmation"]
        assert order_dispatched == confirmation_page.confirmation_messages["order_dispatched"]
        assert confirmation_page.pathUrl in web.current_url
        # Back To Home Page
        confirmation_page.back_to_home_page()
        assert inventory_page.pathUrl in web.current_url


if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
