
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

#Buscar 
tab_link: WebElement = driver.find_element(By.LINK_TEXT, 'Tablets')
tab_link.click()

item: WebElement = driver.find_element(By.LINK_TEXT, 'Samsung Galaxy Tab 10.1')
item.click()

#Checar precio, agregar al carrito y a wishlist
price: WebElement = driver.find_element(By.XPATH, "//ul[@class='list-unstyled']//h2")
assert price.text == "$241.99"
wish_button: WebElement = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div[1]/button[1]')
wish_button.click()
cart_button: WebElement = driver.find_element(By.ID, 'button-cart')
cart_button.click()

#Cerrar navegador
driver.quit()