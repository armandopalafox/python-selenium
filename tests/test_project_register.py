from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.register_page import RegisterPage

class TestProjectRegister:
    driver: WebDriver = None
    register_page: RegisterPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=account/register")
        self.register_page = RegisterPage(self.driver)


    def test_case_1(self):
        self.register_page.fill_form()
        self.register_page.register_invalid()
        self.register_page.accept_policy()
        self.register_page.send_form()
        email_validation = self.driver.find_element(By.ID,'input-email').get_attribute('validationMessage')
        assert email_validation

    def test_case_2(self):
        # Funciona solo la primera vez, con el mismo email
        self.register_page.fill_form()
        self.register_page.register_valid()
        self.register_page.accept_policy()
        self.register_page.send_form()
        success_msg = self.driver.find_element(By.XPATH,"//*[@id='content']/h1")
        assert success_msg.text == 'Your Account Has Been Created!'
       
    def test_case_3(self):
        self.register_page.fill_form()
        self.register_page.register_valid()
        self.register_page.send_form()
        alert_msg = self.driver.find_element(By.XPATH, "//*[@id='account-register']//div[text()=' Warning: You must agree to the Privacy Policy!']")
        assert alert_msg.text =='Warning: You must agree to the Privacy Policy!'
        
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()