import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.testbase import SortableListPage
import time
class TestSortableList:
    @pytest.fixture
    def web(self):
        driver = WebDriver()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_sortable_list_one_item(self, web: WebDriver):
        """Prueba arrastrar 'Larry Page' a la primera posición."""
        page = SortableListPage(web)
        page.visit_url()
        
        # Obtener la lista de nombres
        items = page.get_person_names()
        larry_page = next((item for item in items if item.text == "Larry Page"), None)
        first_item = items[0]
        
        assert larry_page is not None, "No se encontró a 'Larry Page' en la lista."
        actions = ActionChains(web)
        actions.drag_and_drop(larry_page, first_item).perform()
        
        items = page.get_person_names() 
        assert items[0].text == "Larry Page", f"Se esperaba 'Larry Page' en la primera posición, pero se encontró '{items[0].text}'."

    def test_sortable_list(self, web: WebDriver):
        """Test ordenar la lista completa según top_list y verificar colores."""
        page = SortableListPage(web)
        page.visit_url()

        title = page.get_title()
        assert "10 Richest People" in title.text, "No se encontró el título esperado."

        top_list = page.get_top_list()

        for index, person in enumerate(top_list):
            page.drag_item_to(person['name'], index)
            time.sleep(0.5)

        page.click_check_button()

        items = page.get_person_names()
        for element in items:
            color = page.get_element_color(element)
            assert color in (page.color_green_rgb, page.color_green_rgba), \
                f"El color del elemento '{element.text}' fue {color}, pero se esperaba {page.color_green_rgb} o {page.color_green_rgba}."

        web.execute_script("document.body.style.zoom='80%'")
        assert web.save_screenshot("sorted_list.png"), "No se pudo guardar el screenshot."
