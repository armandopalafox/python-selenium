from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.login_page import LoginPage

class TestProjectLogin:
    driver: WebDriver = None
    login_page: LoginPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=account/login")
        self.login_page = LoginPage(self.driver)

    def test_case_1(self):
        self.login_page.login("armando@yopmail.com", "INVALID_PASSWORD")
        assert self.login_page.is_login_warn_displayed(), "Warn should be displayed"

    def test_case_2(self):
        self.login_page.login("pepe@yopmail.com", "123456")
        
        assert self.login_page.my_account_msg_displayed(), "My Account text should be visible"
    
    def test_case_3(self):
        
        assert self.login_page.forgotten_password() == 'An email with a confirmation link has been sent your email address.'
    
    def teardown_method(self):
        if self.driver:
            self.driver.quit()