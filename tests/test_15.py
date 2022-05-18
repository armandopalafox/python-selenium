import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from sniffio import current_async_library
from lib.factory.factory_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lib.config import config

class TestCurrency():

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())
        self.driver.get(config.get_url())

    def test(self):
        
        #Currency
        currency_loc = (By.XPATH, "//*[@id='form-currency']//strong")
        currency: WebElement = self.wait.until(EC.visibility_of_element_located(currency_loc))
        assert currency.text == '$'

        #Search
        search_loc = (By.NAME, 'search')
        search: WebElement = self.wait.until(EC.element_to_be_clickable(search_loc))
        search.send_keys('Samsung')

        #Button
        btn_loc = (By.XPATH, "//*[@id='search']/span/button")
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(btn_loc))
        search_btn.click()
        
        #Samsung
        samsung_loc = (By.LINK_TEXT, 'Samsung SyncMaster 941BW')
        samsung: WebElement = self.wait.until(EC.element_to_be_clickable(samsung_loc))
        samsung.click()

        price_loc = (By.XPATH, "//*[@id='content']//li//h2")
        price: WebElement = self.wait.until(EC.visibility_of_element_located(price_loc))
        price_usd = float(price.text[1:])

        dropdown_loc = (By.XPATH, "//*[@id='form-currency']//button[@data-toggle='dropdown']")
        dropdown: WebElement =  self.wait.until(EC.element_to_be_clickable(dropdown_loc))
        dropdown.click()

        euro_btn_loc = (By.NAME, 'EUR')
        euro_btn: WebElement = self.wait.until(EC.element_to_be_clickable(euro_btn_loc))
        euro_btn.click()

        price: WebElement = self.wait.until(EC.visibility_of_element_located(price_loc))
        price_eur = float(price.text[:-1])

        assert price_usd > price_eur
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()