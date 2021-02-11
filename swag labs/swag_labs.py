import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# PATH = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe') #driver path
driver.get("https://www.saucedemo.com/inventory.html")
# link = driver.find_element_by_link_text ("ADD TO CART")
time.sleep(2)
driver.find_element_by_class_name('btn_primary.btn_inventory').click()
driver.find_element_by_class_name('btn_primary.btn_inventory').click()
driver.find_element_by_class_name('btn_primary.btn_inventory').click()
driver.find_element_by_class_name('btn_primary.btn_inventory').click()
driver.get('https://www.saucedemo.com/cart.html')
driver.find_element_by_class_name('btn_action.checkout_button').click()
time.sleep(1)
first = driver.find_element_by_id('first-name').send_keys('Milind')
last = driver.find_element_by_id('last-name').send_keys('Patil')
zip = driver.find_element_by_id('postal-code').send_keys('400605')
driver.find_element_by_class_name('btn_primary.cart_button').click()
time.sleep(10)
#driver.close()






# link.click()

#driver.quit()
