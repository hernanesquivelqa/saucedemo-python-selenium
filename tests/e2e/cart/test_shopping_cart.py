from tests.testbase import *
from config import BASE_URL, USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO, USERNAME_DEMOQA, LASTNAME_SAUCEDEMO, POSTAL_CODE_SAUCEDEMO
import time

class TestShoppingCart:

    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        login_page = LoginPage(self.driver)
        login_page.submit_login_form(USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO)

        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.shopping_cart_button = self.shopping_cart_page.shopping_cart_button

        assert self.driver.current_url == f"{BASE_URL}/inventory.html", "The redirection to the inventory page was not successful."
        assert self.shopping_cart_button.is_displayed(), "The shopping cart button is not present in the UI."

        yield self.driver

        self.shopping_cart_page.click_burger_button()
        self.shopping_cart_page.log_out_button_click()
        self.driver.quit()
   
    def test_01_assert_browser_title(self, web: WebDriver):
        assert "Swag Labs" in web.title
    def test_02_add_to_cart(self, web: WebDriver):
        shopping_cart_page = ShoppingCartPage(web)

        product_name = shopping_cart_page.add_first_product_to_cart()
        shopping_cart_page.go_to_cart()

        assert "cart.html" in web.current_url, "Did not redirect to the cart page."
        assert product_name == shopping_cart_page.get_first_product_name_in_cart(), "The product in the cart does not match the added one."
   
    def test_03_checkout_one_item(self, web: WebDriver):
        shopping_cart_page = ShoppingCartPage(web)
        product_name = shopping_cart_page.add_first_product_to_cart()
        shopping_cart_page.go_to_cart()
        assert "cart.html" in web.current_url, "Did not redirect to the cart page."
        assert product_name == shopping_cart_page.get_first_product_name_in_cart(), "The product in the cart does not match the added one."
        self.driver.find_element(By.CSS_SELECTOR,'[data-test="checkout"]').click()
        #Checkout Step One
        assert "checkout-step-one.html" in web.current_url,'Did not redirect to the cart page.'
        checkOutStepOnePage = CheckOutStepOnePage(web)
        checkOutStepOnePage.fill_out_form_and_continue(USERNAME_DEMOQA, LASTNAME_SAUCEDEMO, POSTAL_CODE_SAUCEDEMO)
        #Checkout Step Two
        assert "checkout-step-two.html" in web.current_url, 'Did not redirect to the cart page'
        self.driver.find_element(By.ID,'finish').click()
        #Checkout Complete
        order_confirmation_message = self.driver.find_element(By.CSS_SELECTOR,'[data-test="complete-header"]').text
        order_confirmation_message_additional =self.driver.find_element(By.CSS_SELECTOR,'[data-test="complete-text"]').text
        assert order_confirmation_message == "Thank you for your order!"
        assert order_confirmation_message_additional  == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        assert "checkout-complete.html" in web.current_url,'Did not redirect to the cart page'
        #Back To Home Page
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="back-to-products"]').click()
        assert "inventory.html" in web.current_url, 'Did not redirect to the cart page'
  
if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
