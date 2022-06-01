from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.search_module import SearchModule

class TestProjectSearch:
    
    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.search_module = SearchModule(self.driver)

    def test_case_1(self):   
        assert self.search_module.search('iPhone').text == 'iPhone'

    def test_case_2(self):
        assert self.search_module.search_invalid('qaminds').text == 'There is no product that matches the search criteria.'

    def teardown_method(self):
        if self.driver:
            self.driver.quit()