from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ShoppingCartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cartItems = self.driver.find_element(By.CSS_SELECTOR, '.inventory_item')
 

    def add_first_product_to_cart(self):
        """Agrega el primer producto disponible al carrito."""
        products_to_add_cart = self.driver.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        assert len(products_to_add_cart) > 0, "No hay productos disponibles para agregar al carrito."

        first_product_button = products_to_add_cart[0]
        product_container = first_product_button.find_element(By.XPATH, './/ancestor::div[@data-test="inventory-item"]')

        # Guardar el nombre del producto para validarlo después
        product_name = product_container.find_element(By.CSS_SELECTOR, '[data-test*="title-link"]').text
        first_product_button.click()
        return product_name

    def go_to_cart(self):
        """Navega hasta la página del carrito."""
        cart = self.driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart.click()

    def get_first_product_name_in_cart(self):
        """Obtiene el nombre del primer producto dentro del carrito."""
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text
    
    
    