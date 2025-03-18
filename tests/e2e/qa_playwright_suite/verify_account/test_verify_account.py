from tests.testbase import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestVerifyAccount:
    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qaplayground.dev/apps/verify-account/')
        yield self.driver
        self.driver.quit()
    def test_fill_inputs(self, web: WebDriver):
        try:
            # Buscar el primer input con type="number"
            input_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="number"]'))
            )[0]
            input_element.send_keys('9')
        except IndexError:
            print("No se encontraron elementos <input type='number'> en la página.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")