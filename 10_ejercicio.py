from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#Setup
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait =  WebDriverWait(driver, 10)

driver.get(url)

#Test logic
btn_locator = (By.ID, 'autoclosable-btn-success')
btn_element: WebElement =  wait.until(EC.element_to_be_clickable(btn_locator))
btn_element.click()

msg_locator = (By.CSS_SELECTOR, '.alert-autocloseable-success')
msg_visible: WebElement = wait.until(EC.visibility_of_element_located(msg_locator))
assert msg_visible.is_displayed(), "Message is visible"
msg_invisible: WebElement = wait.until(EC.invisibility_of_element_located(msg_locator))

# Close browser
driver.quit()