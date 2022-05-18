from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lib.config import config

class TestiMac():

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())
        self.driver.get(config.get_url())

    def test(self):

        #Desktop
        desktop_loc = (By.LINK_TEXT, 'Desktops')
        desktop: WebElement = self.wait.until(EC.element_to_be_clickable(desktop_loc))
        desktop.click()

        #Mac
        mac_loc = (By.PARTIAL_LINK_TEXT, 'Mac')
        mac: WebElement = self.wait.until(EC.element_to_be_clickable(mac_loc))
        mac.click()
        iMac_loc = (By.LINK_TEXT, 'iMac')
        iMac: WebElement = self.wait.until(EC.element_to_be_clickable(iMac_loc))
        iMac.click()

        #Cart
        cart_btn_loc = (By.ID, 'button-cart')
        cart_btn: WebElement = self.wait.until(EC.element_to_be_clickable(cart_btn_loc))
        cart_btn.click()

        #Validation
        msg_success_loc = (By.CLASS_NAME, 'alert-success')
        msg_success = 'Success: You have added '
        assert self.wait.until(EC.text_to_be_present_in_element(msg_success_loc, msg_success))

        #Price
        price_loc = (By.ID, 'cart-total')
        expected_price = '1 item(s) - $122.00'
        assert self.wait.until(EC.text_to_be_present_in_element(price_loc, expected_price))
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()