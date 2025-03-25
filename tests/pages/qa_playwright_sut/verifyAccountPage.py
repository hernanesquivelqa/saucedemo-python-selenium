from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tests.utils.locators import Locators

class VerifyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators(driver)
        self.url = "https://qaplayground.dev/apps/verify-account/"
        self.input_locator = 'input[type="number"]'
        self.success_locator = 'small.info.success'

    def wait_for_elements(self, locator: str, timeout: int = 10):
        """Espera y retorna todos los elementos que coinciden con el locator."""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator))
            )
            return elements
        except TimeoutException:
            raise TimeoutException(f"No se encontraron elementos con locator '{locator}' después de {timeout} segundos")

    def wait_for_element(self, locator: str, index: int = 0, timeout: int = 10):
        """Espera y retorna el elemento en la posición 'index' que coincide con el locator."""
        elements = self.wait_for_elements(locator, timeout)
        if not elements or len(elements) <= index:
            raise IndexError(f"Solo se encontraron {len(elements)} elementos, índice {index} fuera de rango")
        return elements[index]

    def send_key(self, key: str = '9'):
        """Envía una tecla al primer input numérico."""
        try:
            input_element = self.wait_for_element(self.input_locator)
            input_element.clear()
            input_element.send_keys(key)
            return True
        except Exception as e:
            print(f"Error al enviar la tecla: {str(e)}")
            return False

    def fill_all_inputs(self, key: str = '9'):
        """Llena todos los inputs numéricos con una tecla específica."""
        try:
            input_elements = self.wait_for_elements(self.input_locator)
            if not input_elements:
                print("No se encontraron inputs de tipo 'number'")
                return False
            for index, input_element in enumerate(input_elements):
                input_element.clear()
                input_element.send_keys(key)
                print(f"Llenado input #{index} con '{key}'")
            return True
        except Exception as e:
            print(f"Error al llenar los inputs: {str(e)}")
            return False

    def get_info_success_text(self, timeout: int = 10):
        """Obtiene el texto del elemento de éxito."""
        try:
            info_success = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.success_locator))
            )
            return info_success.text
        except TimeoutException:
            print(f"No se encontró el elemento '{self.success_locator}' después de {timeout} segundos")
            return None
        except Exception as e:
            print(f"Error al obtener el texto de éxito: {str(e)}")
            return None

    def open(self):
        """Abre la página."""
        self.driver.get(self.url)