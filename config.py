from dotenv import load_dotenv
import os
import random

load_dotenv()

USERNAME_SAUCEDEMO = os.getenv("USERNAME_SAUCEDEMO")
PASSWORD_SAUCEDEMO = os.getenv("PASSWORD_SAUCEDEMO")
USERNAME_DEMOQA = os.getenv("USERNAME_DEMOQA")
PASSWORD_DEMOQA = os.getenv("PASSWORD_DEMOQA")
USER_ID_DEMOQA= os.getenv("USER_ID_DEMOQA")
BASE_URL = os.getenv("BASE_URL")
BEARER_DEMOQA = os.getenv("BEARER_DEMOQA")
LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER")
PROBLEM_USER = os.getenv("PROBLEM_USER")
INVALID_USERNAME = os.getenv("INVALID_USERNAME")
random_num = random.randint(0,8)