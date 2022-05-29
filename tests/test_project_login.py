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

    def test_invalid_login(self):
        self.login_page.login("invalid@gmail.com", "INVALID_PASSWORD")
        assert self.login_page.is_login_warn_displayed(), "Warn should be displayed"

    def test_forgoten_password(self):
        self.login_page.forgotten_password()

    def test_continue_as_new_customer(self):
        self.login_page.continue_as_new_customer()

    def test_select_menu(self):
        for menu in ['Login', 'Register', 'My Account', 'Address Book']:
            self.login_page.select_menu(menu)
    
    def teardown_method(self):
        if self.driver:
            self.driver.quit()