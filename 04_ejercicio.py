
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
laptops_tab: WebElement = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
laptops_tab.click()
windows: WebElement = driver.find_element(By.LINK_TEXT, "Windows (0)")
windows.click()

message: WebElement = driver.find_element(By.XPATH, "//div[@id='content']/p")
assert message.is_displayed(), "El texto no fue encontrado"
assert message.text == "There are no products to list in this category." 
continue_button: WebElement = driver.find_element(By.LINK_TEXT, "Continue")
continue_button.click()

driver.quit()