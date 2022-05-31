from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage

class TestProjectProduct:
    driver: WebDriver = None
    product_page: ProductPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=product/product&path=20_27&product_id=41")
        self.product_page = ProductPage(self.driver)

    def test_case_1(self):
        product_name = 'iMac'
        assert self.product_page.get_name() == product_name
        product_price = '$122.00'
        assert self.product_page.get_price() == product_price
        product_code = 'Product 14'
        assert self.product_page.get_product_code() == product_code
        product_availability = 'In Stock'
        assert self.product_page.get_availability() == product_availability
        
    def test_case_2(self):
        msg = 'Thank you for your review. It has been submitted to the webmaster for approval.'
        assert self.product_page.make_review() == msg

    def test_case_3(self):
        self.product_page.see_product_img()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()