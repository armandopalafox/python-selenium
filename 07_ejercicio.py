from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Setup
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://demo.seleniumeasy.com/'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait =  WebDriverWait(driver, 10)

driver.get(url)

#Test logic
locator = (By.ID, 'at-cv-lightbox-close')
close_btn: WebElement =  wait.until(EC.element_to_be_clickable(locator))
assert close_btn.is_enabled(), "pop close button is not enabled"
close_btn.click()

driver.quit()