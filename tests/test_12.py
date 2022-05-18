from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lib.config import config

class TestDowload():
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
        
        # Click download
        dw_locator = (By.ID, 'downloadButton')
        download_btn: WebElement =  self.wait.until(EC.element_to_be_clickable(dw_locator))
        download_btn.click()

        complete_locator = (By.CSS_SELECTOR, '.progress-label')
        # assert wait.until(EC.text_to_be_present_in_element(complete_locator, "Complete")), "Complete not visible"
        self.wait.until(EC.text_to_be_present_in_element(complete_locator, 'Complete'))

        close_locator = (By.XPATH, "//button[text()='Close']") 
        close_btn: WebElement =  self.wait.until(EC.element_to_be_clickable(close_locator))
        close_btn.click()

    def test_download_button_2(self):
        """Ejercicio 9"""
        # Open web page
        self.driver.get('https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html')

        dw_locator = (By.ID, 'cricle-btn')
        download_btn: WebElement =  self.wait.until(EC.element_to_be_clickable(dw_locator))
        download_btn.click()

        percent_locator = (By.CSS_SELECTOR, '.percenttext')
        assert self.wait.until(EC.text_to_be_present_in_element(percent_locator, "100%")), "Download is not complete"

    def test_download_button_3(self):
        """Ejercicio 10"""
        self.driver.get('https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html')

        btn_locator = (By.ID, 'autoclosable-btn-success')
        btn_element: WebElement =  self.wait.until(EC.element_to_be_clickable(btn_locator))
        btn_element.click()

        msg_locator = (By.CSS_SELECTOR, '.alert-autocloseable-success')
        self.wait.until(EC.visibility_of_element_located(msg_locator))
        assert self.wait.until(EC.invisibility_of_element_located(msg_locator)), "NOT found"


    def teardown_method(self):
        if self.driver:
            self.driver.quit()