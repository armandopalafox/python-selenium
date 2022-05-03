# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.maximize_window()
driver.implicitly_wait(3)
#Abrir página
driver.get(url)

#Test logic
account: WebElement = driver.find_element(By.XPATH, "//a[@title='My Account']")
account.click()
login: WebElement = driver.find_element(By.LINK_TEXT, "Login")
login.click()

email_input: WebElement = driver.find_element(By.XPATH, '//input[@name="email"]')
email_input.send_keys('armando@yopmail.com')
password_input: WebElement = driver.find_element(By.XPATH, '//input[@name="password"]')
password_input.send_keys('123456')
login_button: WebElement = driver.find_element(By.XPATH, "//input[@value='Login']")
login_button.click()

message: WebElement = driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]')
assert message.is_displayed(), 'El mensaje no es mostrado'

# time.sleep(5)
driver.quit()