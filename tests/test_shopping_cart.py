from tests.testbase import *
from config import BASE_URL, USERNAME_SAUCEDEMO, PASSWORD_SAUCEDEMO
class TestShoppingCart:
    
    @pytest.fixture
    def web(self):
      
        driver = webdriver.Chrome()
        driver.get(BASE_URL)
        login_page = LoginPage(driver)
        login_page.enterUsername(USERNAME_SAUCEDEMO)
        login_page.enterPassword(PASSWORD_SAUCEDEMO)
        login_page.clickSubmit()
        shopping_cart_button = driver.find_element(By.ID,'shopping_cart_container')
        assert driver.current_url == f"{BASE_URL}/inventory.html", "No se redirigió correctamente a la página de inventario."
        assert shopping_cart_button.is_displayed(),'No esta el botón de shopping cart presente en la UI'
        yield driver  
        driver.quit()

    def test_01_assert_browser_title(self, web: WebDriver):
        assert "Swag Labs" in web.title

    def test_02_add_to_cart(self, web: WebDriver):
        shopping_cart = ShoppingCartPage(web)

        product_name = shopping_cart.add_first_product_to_cart()
        shopping_cart.go_to_cart()

        assert 'cart.html' in web.current_url, "No se redirigió a la página del carrito."
        assert product_name == shopping_cart.get_first_product_name_in_cart(), "El producto en el carrito no coincide con el agregado."
