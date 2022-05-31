from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage

class TestProjectHome:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
    

    def test_case_1(self):   
        home_page = HomePage(self.driver)
        home_page.select_sub_menu("Desktops", "Mac (1)")
        home_page.select_product('iMac')
        home_page.add_to_cart()
        
        total = home_page.get_cart_total()
        assert total == "1 item(s) - $122.00"

    def test_case_2(self):
        #Aquí a veces sale un Timeout, pero pienso que es por la velocidad de mi equipo
        home_page = HomePage(self.driver)
        home_page.select_product('iPhone')
        assert home_page.add_to_wl() == 'Wish List (1)'    
    
    def test_case_3(self):
        home_page = HomePage(self.driver)
        assert "$" == home_page.get_currency()
        home_page.set_currency("EUR")
        assert "€" == home_page.get_currency()


    def teardown_method(self):
        if self.driver:
            self.driver.quit()