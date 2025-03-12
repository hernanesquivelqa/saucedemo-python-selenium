from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Locators:
    def __init__(self, driver: WebDriver):
        self.web = driver

    def by_data_test(self, data_test: str):
        return self.web.find_element(By.CSS_SELECTOR, f"[data-test={data_test}]")
