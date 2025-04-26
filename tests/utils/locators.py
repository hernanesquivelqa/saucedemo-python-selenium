from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Locators:
    def __init__(self, driver: WebDriver):
        self.web = driver

    def by_data_test(self, data_test: str):
        return self.web.find_element(By.CSS_SELECTOR, f"[data-test={data_test}]")
    def by_class_Name(self, data_test: str):
        return self.web.find_elements(By.CSS_SELECTOR, f"{data_test}")
    def by_xpath(self, data_test: str):
        return self.web.find_element(By.XPATH, f"{data_test}")
