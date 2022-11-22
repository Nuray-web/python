categorys = {'Утюги': 'https://www.technodom.kz/catalog/bytovaja-tehnika/uhod-za-odezhdoj/utjugi', 
             'Парогенераторы': 'https://www.technodom.kz/catalog/bytovaja-tehnika/uhod-za-odezhdoj/utjugi-s-parogeneratorom', 
             'Отпариватели': 'https://www.technodom.kz/catalog/bytovaja-tehnika/uhod-za-odezhdoj/otparivateli-dlja-odezhdy', 
             'Гладильные доски':'https://www.technodom.kz/catalog/bytovaja-tehnika/uhod-za-odezhdoj/gladil-nye-doski'}

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import math

def parse_category(category_name,category_link):
    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    action = webdriver.ActionChains(driver)
    driver.get(category_link)
    driver.maximize_window()
    
    action.move_by_offset(10, 20)    # 10px to the right, 20px to bottom
    action.click().perform()
    
    
    df = []
    qty_of_all_products = driver.find_element(By.XPATH, '//p[@class="category-page-list__subtitle"]').text.strip().replace(' товара', '').replace('Найдено ', '').replace(' товаров', '')
    qty_per_page = driver.find_elements(By.XPATH, '//div[@class="ProductCardV category-page-list__product"]')
    qty_page = math.ceil(int(qty_of_all_products)/(len(qty_per_page)*2))
    print("Количество страниц", qty_page)
    
    for i in range(1, qty_page+1):
        new_url = category_link + '?page=' + str(i)
        print('\n', new_url, '\n')
        driver.get(new_url)
        action.move_by_offset(10, 20)    # 10px to the right, 20px to bottom
        action.click().perform()
    
        driver.execute_script("window.scrollBy(0, 1500);")
        driver.implicitly_wait(10)
        time.sleep(5)
    
        soup = BeautifulSoup(driver.page_source)
        products = soup.find_all('div', class_='ProductCardV category-page-list__product')
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
    driver.close()
    data.to_csv('C:/Users/nsyrymbet/Desktop/test_parsing/'+'TD '+str(category_name)+'.csv', encoding='utf-8-sig', index = False)
    
for k,v in categorys.items():
    print('Категория:', k, '\nСсылка:', v)
    parse_category(k,v)
