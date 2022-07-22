import urllib.request
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/nsyrymbet/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.google.kz/imghp?hl=ru&authuser=0&ogbl")

input_name = driver.find_element(By.XPATH, "//input")
input_name.send_keys("TW1923RH")

search_button = driver.find_element(By.XPATH, "//button[@type = 'submit']")
search_button.click()

pic = driver.find_element(By.XPATH, "//img[@class = 'rg_i Q4LuWd']")
src = pic.get_attribute('src')

# download the image
urllib.request.urlretrieve(src, "TW1923RH.png")

time.sleep(10)

driver.close()
