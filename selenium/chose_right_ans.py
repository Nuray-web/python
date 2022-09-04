from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try: 
    num1 = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    print(num1)
    num2 = browser.find_element(By.XPATH, '//span[@id="num2"]').text
    print(num2)
    ans = int(num1) + int(num2)
    print(ans)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(ans))
        
    submit = browser.find_element(By.XPATH, '//button')
    submit.click()
    
finally:
    time.sleep(5)
    browser.quit()
