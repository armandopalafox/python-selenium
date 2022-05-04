from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Setup
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait =  WebDriverWait(driver, 25)

driver.get(url)

#Test logic
dw_locator = (By.ID, 'cricle-btn')
download_btn: WebElement =  wait.until(EC.element_to_be_clickable(dw_locator))
download_btn.click()

percent_locator = (By.CSS_SELECTOR, '.percenttext')
assert wait.until(EC.text_to_be_present_in_element(percent_locator, "100%")), "Download is not complete"

# Close browser
driver.quit()