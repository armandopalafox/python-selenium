
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lib.config import config

class TestDisplay():

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())
        self.driver.get(config.get_url())

    def test(self):

        #Search input
        search_loc = (By.CLASS_NAME, 'input-lg')
        search: WebElement = self.wait.until(EC.element_to_be_clickable(search_loc))
        search.send_keys('Display')

        #Search button
        btn_loc = (By.XPATH, '//*[@id="search"]/span/button')
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(btn_loc))
        search_btn.click()

        #No products msg
        products_msg_loc = (By.XPATH, "//*[@id='button-search']/following-sibling::p")
        no_products_msg = 'There is no product that matches the search criteria.'
        assert self.wait.until(EC.text_to_be_present_in_element(products_msg_loc, no_products_msg))
        # //p[text()='There is no product that matches the search criteria.']

        #Checkbox
        checkbox_loc = (By.ID, 'description')
        checkbox: WebElement = self.wait.until(EC.element_to_be_clickable(checkbox_loc))
        checkbox.click()
        assert checkbox.is_selected()

        #Search 2
        search2: WebElement = self.driver.find_element(By.ID, 'button-search')
        search2.click()

        for product_name in ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']:
            loc = (By.LINK_TEXT, product_name)
            product_item: WebElement = self.wait.until(EC.element_to_be_clickable(loc))
            assert product_item.is_displayed()

        #Find all products
        products_loc = (By.XPATH, "//*[@class='caption']//a")
        products: list = self.wait.until(EC.visibility_of_all_elements_located(products_loc))
        for product in products:
            assert product.text in ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']

    def teardown_method(self):
        if self.driver:
            self.driver.quit()