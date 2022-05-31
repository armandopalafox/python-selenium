from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.checkout_page import CheckoutPage

class TestProjectCheckout:
    driver: WebDriver = None
    checkout_page: CheckoutPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get("https://laboratorio.qaminds.com/index.php?route=common/home")
        self.checkout_page = CheckoutPage(self.driver)


    def test_case_1(self):
        self.checkout_page.add_cart()
        self.checkout_page.guest_checkout()

        # Step 2 debe decir: Billing Details, y no Account & Billing Details
        step2 = self.driver.find_element(By.XPATH, "//a[@class='accordion-toggle']")
        assert step2.text == 'Step 2: Billing Details'

    def test_case_2(self):
        self.checkout_page.add_cart()
        self.checkout_page.login_checkout()
        # Step 2 debe decir: Billing Details, y no Account & Billing Details
        step2 = self.driver.find_element(By.XPATH, "//a[@class='accordion-toggle']")
        assert step2.text == 'Step 2: Billing Details'

    def test_case_3(self):
        # Validar que no puede hacer checkout con el carrito vacío
        assert self.checkout_page.fail_checkout() == 'Your shopping cart is empty!'
        
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()