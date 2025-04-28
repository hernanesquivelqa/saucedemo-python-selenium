from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.utils.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
class SortableListPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qaplayground.dev/apps/sortable-list/"
        self.locators = Locators(self.driver)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.color_green_rgb = "rgb(58, 227, 116)"
        self.color_green_rgba = "rgba(58, 227, 116, 1)"
        self.top_list = [
            {"position": 1, "name": "Jeff Bezos"},
            {"position": 2, "name": "Bill Gates"},
            {"position": 3, "name": "Warren Buffett"},
            {"position": 4, "name": "Bernard Arnault"},
            {"position": 5, "name": "Carlos Slim Helu"},
            {"position": 6, "name": "Amancio Ortega"},
            {"position": 7, "name": "Larry Ellison"},
            {"position": 8, "name": "Mark Zuckerberg"},
            {"position": 9, "name": "Michael Bloomberg"},
        ]

    def visit_url(self):
        """Navega a la URL de la página."""
        self.driver.get(self.url)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "person-name")))

    def get_person_names(self):
        """Obtiene la lista de elementos con nombres de personas."""
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "person-name")))

    def get_title(self):
        """Obtiene el elemento del título."""
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '10 Richest People')]")))

    def get_top_list(self):
        """Devuelve la lista predefinida de personas más ricas."""
        return self.top_list

    def click_check_button(self):
        """Hace clic en el botón 'Check'."""
        check_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#check")))
        check_button.click()

    def get_element_color(self, element):
        """Obtiene el color de un elemento."""
        return element.value_of_css_property("color")
    
    def drag_item_to(self, source_name: str, target_index: int):
        """
        Drags the item with text source_name into the position target_index in the list
        """
        items = self.get_person_names()
        source = next((el for el in items if el.text == source_name), None)
        if not source:
            raise ValueError(f"Item '{source_name}' not found on page")
        target_items = self.get_person_names()
        if target_index < 0 or target_index >= len(target_items):
            raise IndexError(f"Target index {target_index} out of bounds")
        target = target_items[target_index]

        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()