from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
url = 'https://www.mechta.kz/section/utyugi-mm7/'
driver.get(url)

time.sleep(10)
button_close = driver.find_element(By.XPATH, '//*[@id="popmechanic-form-37872"]/div[3]')
button_close.click()

#button_close = driver.find_element(By.XPATH, '//*[@id="popmechanic-form-37872"]/div[3]')
#button_close.click()



another_button = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/div/div[1]/div')
another_button.click()

soup = BeautifulSoup(driver.page_source)
products = soup.find_all('div', class_="hoverCard")


df = []

for i in products:    
    title = i.find('div', class_ = 'q-pt-md q-mt-xs q-px-md text-ts3 text-color2 ellipsis').text.strip()
    price1 = i.find('div',class_ = 'text-ts1 text-bold q-mr-md text-black').text.strip().replace('\xa0', '').replace(' тг.', '')
    try:
        percentage = int(i.find('div',class_ = 'die-lg-discount bg-white q-px-xs q-pr-sm q-pl-sm text-primary text-weight-bold').text.strip().replace('-', '').replace('%', ''))
        print(percentage, type(percentage))
        price2 = price1 * (1 - (int(percentage)/100))
        print(price2)
    except:
        price2 = price1
    row = {'Время':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Название': title, 'Итоговая Цена': price1, 'Формальная Цена': price2}
    print(row)
    df.append(row)
        
        
data = pd.DataFrame(data = df)
data
