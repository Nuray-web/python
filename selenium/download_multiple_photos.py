import urllib.request
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/nsyrymbet/Downloads/chromedriver_win32/chromedriver.exe")

products = ['TX9736WO', 'TY6543RH', 'TY6545RH', 'TY6547RH','TY6735WH','TY6737 WH','TY6751WO','TY6756WO','TY6753WO',
            'TY9133WH','TY9152WO','TY9171WO','TY9179WO', 'TY6933WO','TY6975WO','TY1127WO', 'TY1129WO', 'TY6838WO',
           'TY6837WO', 'TY6878WO', 'TY9639WO', 'TY9679WO', 'TY9691W0', 'TY9690WO', 'TY2039WO', 'TY2079WO', 'TY9479WO',
           'TY9472WO', 'TY9471WO', 'TY9490WO', 'TY9879WO', 'TY9890WO', 'TY98A9WO', 'TY98C0WO', 'TY9958WO', 'TY9990WO',
           'TY99F1WO']

for product in products:
    driver.get("https://www.google.kz/imghp?hl=ru&authuser=0&ogbl")

    input_name = driver.find_element(By.XPATH, "//input")
    input_name.send_keys(product)

    search_button = driver.find_element(By.XPATH, "//button[@type = 'submit']")
    search_button.click()

    pic = driver.find_element(By.XPATH, "//img[@class = 'rg_i Q4LuWd']")
    src = pic.get_attribute('src')

    urllib.request.urlretrieve(src, product+".jpeg")

time.sleep(10)

driver.close()
