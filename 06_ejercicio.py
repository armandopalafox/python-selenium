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
driver.implicitly_wait(5)

driver.get(url)
cars_menu: WebElement = driver.find_element(By.ID, "cars")
assert cars_menu.is_displayed(), "El menu no es visible"
cars_dropdown =  Select(cars_menu)

cars_dropdown.select_by_visible_text("Volvo")
cars_dropdown.select_by_visible_text("Audi")
selected_options: list = [option.text for option in cars_dropdown.all_selected_options]
assert "Volvo" in selected_options, "Volvo is not selected"
assert "Audi" in selected_options, "Audi is not selected"

time.sleep(3)
driver.quit()