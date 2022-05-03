import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

#Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url= 'https://demoqa.com/select-menu'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.maximize_window()

driver.get(url)
time.sleep(5)
color_menu: WebElement = driver.find_element(By.ID, "oldSelectMenu")
assert color_menu.is_displayed(), "El menu no es visible"
color_dropdown =  Select(color_menu)
color_dropdown.select_by_visible_text("Green")
selected_option: WebElement = color_dropdown.first_selected_option
assert selected_option.text == "Green", "Green is not selected"
time.sleep(3)
driver.quit()