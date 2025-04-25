import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
class TestSortableList:
    @pytest.fixture
    def web(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()
    def test_sortable_list_one_item(self, web: webdriver.Chrome):
        web.get("https://qaplayground.dev/apps/sortable-list/")
        items = web.find_elements(By.CSS_SELECTOR, ".person-name")
        larry_page = next((item for item in items if item.text == "Larry Page"), None)
        first_item = items[0]
        actions = ActionChains(web)
        actions.drag_and_drop(larry_page, first_item).perform()
        time.sleep(2)
        

    def test_sortable_list(self, web: webdriver.Chrome):
        web.get("https://qaplayground.dev/apps/sortable-list/")
        title = web.find_element(By.XPATH, "//h1[contains(text(), '10 Richest People')]")
        assert "10 Richest People" in title.text, "No se encontró el título esperado" 
        
        items = web.find_elements(By.CSS_SELECTOR, ".person-name")
        top_list = [
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
        time.sleep(2)

