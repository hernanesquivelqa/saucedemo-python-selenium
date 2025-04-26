import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from tests.pages.loginPage import LoginPage
from tests.pages.qa_playwright_sut.verifyAccountPage import VerifyAccountPage
from tests.pages.cart.shoppingCartInventoryPage import ShoppingCartInventoryPage
from tests.pages.cart.checkOutStepOnePage import CheckOutStepOnePage
from tests.pages.qa_playwright_sut.sortableListPage import SortableListPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.cart.cartPage import CartPage
from tests.pages.cart.checkoutCompletePage import CheckOutCompletePage
from selenium.common.exceptions import TimeoutException

from selenium import webdriver

def take_fullpage_screenshot(driver, file_name):
 
    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    
    driver.set_window_size(required_width, required_height)
    driver.save_screenshot(file_name)
    driver.set_window_size(original_size['width'], original_size['height'])


