from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Setup
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait =  WebDriverWait(driver, 10)

driver.get(url)

#Test logic
dw_locator = (By.ID, 'downloadButton')
download_btn: WebElement =  wait.until(EC.element_to_be_clickable(dw_locator))
download_btn.click()

complete_locator = (By.CSS_SELECTOR, '.progress-label')
# assert wait.until(EC.text_to_be_present_in_element(complete_locator, "Complete")), "Complete not visible"
complete_msg: WebElement =  wait.until(EC.visibility_of_element_located(complete_locator))
assert complete_msg.is_displayed(), "message is not visible"

close_locator = (By.XPATH, "//button[text()='Close']") 
close_btn: WebElement =  wait.until(EC.element_to_be_clickable(close_locator))
close_btn.click()

# Close browser
driver.quit()