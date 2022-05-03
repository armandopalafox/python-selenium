
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
driver.implicitly_wait(5)
#Abrir página
driver.get(url)

#Buscar 
search: WebElement = driver.find_element(By.XPATH, "//input[@name='search']")
assert search.is_displayed(), "No se encontro el elemento"
search.clear()
search.send_keys("iphone")

button: WebElement = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
button.click()
iphone: WebElement = driver.find_element(By.XPATH, "//img[@alt='iPhone']")
assert iphone.is_displayed(), "No se encontró la imagen"

#Cerrar navegador
driver.quit()