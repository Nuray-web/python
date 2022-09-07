from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try: 
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    print(x)

    x_val = math.log(abs(12*math.sin(int(x))))
    
    input_x = browser.find_element(By.XPATH, "//input")
    input_x.send_keys(x_val)
    
    select_cb = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    select_cb.click()
    
    browser.execute_script("window.scrollBy(0, 100);")
    select_rb = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    select_rb.click()
                       
    submit = browser.find_element(By.XPATH, '//button')
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
