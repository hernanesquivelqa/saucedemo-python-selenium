from dotenv import load_dotenv
import os

load_dotenv()

USERNAME_SAUCEDEMO = os.getenv('USERNAME_SAUCEDEMO')
PASSWORD_SAUCEDEMO = os.getenv('PASSWORD_SAUCEDEMO')
BASE_URL = os.getenv('BASE_URL')