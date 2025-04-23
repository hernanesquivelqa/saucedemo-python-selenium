from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartInventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.pathUrl = "https://www.saucedemo.com"
        # Definiendo solo los localizadores
        self.cart_items_locator = (By.CSS_SELECTOR, ".inventory_item")
        self.shopping_cart_link_locator = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        self.burger_menu_button_locator = (By.ID, "react-burger-menu-btn")
        self.log_out_button_locator = (By.CSS_SELECTOR, '[data-test="logout-sidebar-link"]')
        self.shopping_cart_button_locator = (By.ID, "shopping_cart_container")
        self.products_cart_locator = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        self.inventory_item = (By.XPATH, './/ancestor::div[@data-test="inventory-item"]')
        self.title_product = (By.CSS_SELECTOR, '[data-test*="title-link"]')
        self.inventory_first_item_name = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        self.error_messages = {"not_match": "The product in the cart does not match the added one."}

    def add_first_product_to_cart(self):
        """Agrega el primer producto disponible al carrito."""
        products_to_add_cart = self.wait.until(
            EC.presence_of_all_elements_located(self.products_cart_locator)
        )
        assert len(products_to_add_cart) > 0, "No hay productos disponibles para agregar al carrito."

        first_product_button = products_to_add_cart[0]
        product_container = first_product_button.find_element(*self.inventory_item)
        product_name = product_container.find_element(*self.title_product).text
        first_product_button.click()
        return product_name

    def go_to_cart(self):
        """Navega hasta la página del carrito."""
        cart = self.wait.until(EC.element_to_be_clickable(self.shopping_cart_link_locator))
        cart.click()

    def get_first_product_name_in_cart(self):
        """Obtiene el nombre del primer producto dentro del carrito."""
        return self.wait.until(
            EC.presence_of_element_located(self.inventory_first_item_name)
        ).text

    def click_burger_button(self):
        hamburger_menu_driver = self.wait.until(EC.element_to_be_clickable(self.burger_menu_button_locator))
        hamburger_menu_driver.click()

    def log_out_button_click(self):
        log_out = self.wait.until(EC.element_to_be_clickable(self.log_out_button_locator))
        log_out.click()
