import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.shoppingCartPage import ShoppingCartPage  # Importamos la clase del POM
from tests.pages.loginPage import LoginPage
from tests.utils.locators import Locators
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


username = os.getenv('USERNAME_SAUCEDEMO')
password = os.getenv('PASSWORD_SAUCEDEMO')
print(username)
class TestShoppingCart:
    
    @pytest.fixture
    def web(self):
      
        driver = webdriver.Chrome()
        
        driver.get('https://www.saucedemo.com')
        locator = Locators(driver)
        login_page = LoginPage(driver, locator)
        
        
        login_page.enterUsername(username)
        login_page.enterPassword(password)
        login_page.clickSubmit()
        
        shopping_cart_button = driver.find_element(By.ID,'shopping_cart_container')
        assert driver.current_url == "https://www.saucedemo.com/inventory.html", "No se redirigió correctamente a la página de inventario."
        assert shopping_cart_button.is_displayed(),'No esta el botón de shopping cart presente en la UI'
        yield driver  
        
      
       
        driver.quit()

    def test_01_assert_browser_title(self, web: WebDriver):
        assert "Swag Labs" in web.title

    def test_02_add_to_cart(self, web: WebDriver):
        shopping_cart = ShoppingCartPage(web)

        product_name = shopping_cart.add_first_product_to_cart()
        shopping_cart.go_to_cart()

        assert 'cart' in web.current_url, "No se redirigió a la página del carrito."
        assert product_name == shopping_cart.get_first_product_name_in_cart(), "El producto en el carrito no coincide con el agregado."
