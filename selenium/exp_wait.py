from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try: 
    #price = browser.find_element(By.XPATH, '//h5[@id="price"]').text
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    browser.find_element(By.XPATH, '//button').click()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    x_value = math.log(abs(12*math.sin(int(x))))
    input_x = browser.find_element(By.XPATH, '//input')
    input_x.send_keys(x_value)
    
    submit = browser.find_element(By.XPATH, '//button[@id ="solve"]')
    submit.click()
    
finally:
    time.sleep(60)
    browser.quit()
