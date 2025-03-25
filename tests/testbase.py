import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.loginPage import LoginPage
from tests.pages.qa_playwright_sut.verifyAccountPage import VerifyAccountPage
from tests.pages.cart.shoppingCartInventoryPage import ShoppingCartInventoryPage
from tests.pages.cart.checkOutStepOnePage import CheckOutStepOnePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.cart.cartPage import CartPage
from tests.pages.cart.checkoutCompletePage import CheckOutCompletePage
from selenium.common.exceptions import TimeoutException