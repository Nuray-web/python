from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try: 
    button = browser.find_element(By.XPATH, '//button')
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    x_value = math.log(abs(12*math.sin(int(x))))
    input_x = browser.find_element(By.XPATH, '//input')
    input_x.send_keys(x_value)
    
    submit = browser.find_element(By.XPATH, '//button')
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
