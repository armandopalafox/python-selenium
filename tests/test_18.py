from selenium.webdriver.remote.webdriver import WebDriver
from lib.config import config
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage

class TestProductPage:
    driver: WebDriver = None
    product_page: ProductPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")
        self.product_page = ProductPage(self.driver)

    def test_get_product_info(self):
        product_name = 'Samsung SyncMaster 941BW'
        assert self.product_page.get_name() == product_name
        product_price = '$242.00'
        assert self.product_page.get_price() == product_price
        product_ex_tax = '$200.00'
        assert self.product_page.get_ex_tax() == product_ex_tax
        product_code = 'Product 6'
        assert self.product_page.get_product_code() == product_code
        product_availability = 'In Stock'
        assert self.product_page.get_availability() == product_availability
        
    def test_add_to_cart(self):
        self.product_page.add_to_cart()        

    def test_get_total_reviews(self):
        total_reviews = '0 reviews'
        self.product_page.get_total_reviews() == total_reviews

    def teardown_method(self):
        if self.driver:
            self.driver.quit()