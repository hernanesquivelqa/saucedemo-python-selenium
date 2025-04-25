
from time import sleep 
from tests.testbase import *

class TestVerifyAccount:
    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        page = VerifyAccountPage(self.driver)
        page.open()
        yield self.driver
        self.driver.quit()

    def test_fill_inputs(self, web): 
        page = VerifyAccountPage(web) 
        result = page.fill_all_inputs('9')  
        assert result, "Failed to send key to input"
        assert page.get_info_success_text() == "Success"
  
 

if __name__ == "__main__":
    # * Ejecución de las pruebas utilizando pytest
    pytest.main()
