from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    button1.click()
    button2 = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    button2.click()
    
    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, '//span[@id = "input_value"]')
    x = x_element.text
    y = calc(x)

        
    inputs = browser.find_element(By.XPATH, '//input[@id="answer"]')
    inputs.send_keys(y)
        
    submit = browser.find_element(By.XPATH, '//button')
    submit.click()
    
finally:
    time.sleep(30)
    browser.quit()
