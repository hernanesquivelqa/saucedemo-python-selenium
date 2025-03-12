import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.loginPage import LoginPage
from tests.pages.cart.shoppingCartPage import ShoppingCartPage
from tests.pages.cart.checkOutStepOnePage import CheckOutStepOnePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
