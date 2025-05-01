from tests.testbase import *
class TestLoginEvilTesting:
    
    @pytest.fixture
    def web(self):
        self.driver = webdriver.Chrome()
        yield self.driver
        self.driver.quit()
        
    def test_login(self, web: WebDriver):
        # Open the login page
        web.get("https://testpages.eviltester.com/styled/cookies/adminlogin.html")

        # Find the username and password fields
        username_field = web.find_element("name", "username")
        password_field = web.find_element("name", "password")

        # Enter the username and password
        username_field.send_keys("Admin")
        password_field.send_keys("AdminPass")

        web.find_element(By.CSS_SELECTOR, "input[type='checkbox']").is_selected()
        web.save_screenshot("checkbox.png")
    
        web.find_element(By.ID, "login").click()
        assert "adminview.html" in web.current_url, "Login failed!"