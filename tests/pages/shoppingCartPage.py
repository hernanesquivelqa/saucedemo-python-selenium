from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ShoppingCartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    # -----------------------------
    # Elements already located
    # -----------------------------    
        self.cartItems = self.driver.find_element(By.CSS_SELECTOR, '.inventory_item')
        self.shopping_cart_link = self.driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    # -----------------------------
    # List of elements
    # -----------------------------    
        self.products_cart = self.driver.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
    # -----------------------------
    # Element locators for future searches
    # -----------------------------
        self.inventory_item = (By.XPATH,'.//ancestor::div[@data-test="inventory-item"]')
        self.title_product = (By.CSS_SELECTOR,'[data-test*="title-link"]' )
        self.inventory_first_item_name = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        
        
    def add_first_product_to_cart(self):
        """Agrega el primer producto disponible al carrito."""
        products_to_add_cart = self.products_cart
        assert len(products_to_add_cart) > 0, "No hay productos disponibles para agregar al carrito."

        first_product_button = products_to_add_cart[0]
        product_container = first_product_button.find_element(*self.inventory_item)

        # Guardar el nombre del producto para validarlo después
        product_name = product_container.find_element(*self.title_product).text
        first_product_button.click()
        return product_name

    def go_to_cart(self):
        """Navega hasta la página del carrito."""
        cart =  self.shopping_cart_link
        cart.click()

    def get_first_product_name_in_cart(self):
        """Obtiene el nombre del primer producto dentro del carrito."""
        return self.driver.find_element(*self.inventory_first_item_name).text
    
    
    