from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

url = 'https://www.technodom.kz/catalog/bytovaja-tehnika/uhod-za-odezhdoj/utjugi'
driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
action = webdriver.ActionChains(driver)
driver.get(url)
driver.maximize_window()

action.move_by_offset(10, 20)    # 10px to the right, 20px to bottom
action.click().perform()

driver.execute_script("window.scrollBy(0, 1500);")
driver.implicitly_wait(10)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
products = soup.find_all('div', class_ = 'ProductCardV category-page-list__product')

#Добавить скролл вверх, чтобы отображались все данные
df = []
#row = {'Время':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Название': title, 'Цена': price}
for i in products:
    title = i.find('p', class_='Typography ProductCardV__Title --loading Typography__Body Typography__Body_Bold').text.strip()
    try:
        price = i.find('p', class_='Typography ProductCardV__Price Typography__Subtitle').text.strip().replace('\xa0', '').replace('₸', '')
        row = {'Time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Title': title, 'Price with discount': price, 'Actual price': price}
    except:
        price1 = i.find('p', class_='Typography ProductCardV__Price ProductCardV__Price_WithOld Typography__Subtitle').text.strip().replace('\xa0', '').replace('₸', '')
        price2 = i.find('p', class_='Typography ProductCardV__OldPrice Typography__Caption Typography__Caption_Strikethrough').text.strip().replace('\xa0', '').replace('₸', '')
        row = {'Time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Title': title, 'Price with discount': price1, 'Actual price': price2}
    print(title)
    df.append(row)
    
data = pd.DataFrame(data = df)

data['Price with discount'] = data['Price with discount'].astype(int)
data['Actual price'] = data['Actual price'].astype(int)
data['Discount(%)'] = round((data['Price with discount']/data['Actual price'] - 1)*100, 2)

data
