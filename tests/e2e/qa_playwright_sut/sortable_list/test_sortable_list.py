import pytest
from tests.testbase import *
import time
class TestSortableList:
    @pytest.fixture
    def web(self):
        # Creación del driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        yield self.driver 
        self.driver.quit() 
    def test_sortable_list_one_item(self, web: webdriver.Chrome):
        page = SortableListPage(web)
        web.get(page.url)
        items = page.get_person_names()
        larry_page = next((item for item in items if item.text == "Larry Page"), None)
        first_item = items[0]
        actions = ActionChains(web)
        actions.drag_and_drop(larry_page, first_item).perform()
        time.sleep(2)
        
    def test_sortable_list(self, web: webdriver.Chrome):
        page = SortableListPage(web)
        page.visit_url()
        title = page.get_title()
        assert "10 Richest People" in title.text, "No se encontró el título esperado" 
    
        top_list = page.get_top_list()

        for index, person in enumerate(top_list):
            # Refrescamos los elementos
            items = page.get_person_names()

            richest_people = next((item for item in items if item.text == person['name']), None)

            targets = page.get_person_names()
            target = targets[index]

            if richest_people and target:
                actions = ActionChains(web)
                actions.click_and_hold(richest_people).move_to_element(target).release().perform()
            time.sleep(0.5)
     
        web.find_element(By.CSS_SELECTOR, "#check").click()
        items = page.get_person_names()

        for item in items:
            color = item.value_of_css_property("color")
            print(f"Color del elemento {item.text}: {color}")
            assert color in (page.color_green_rgb, page.color_green_rgba),f"The color of the element '{item.text}' was {color}, but it was not the expected value."
        
        web.execute_script("document.body.style.zoom='80%'")
        web.save_screenshot("sorted_list.png")
      

        