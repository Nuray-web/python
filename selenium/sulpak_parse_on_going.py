from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

categorys = {'Утюги': 'https://www.sulpak.kz/f/utyugi', 'Парогенераторы': 'https://www.sulpak.kz/f/parogeneratoriy', 
             'Отпариватели': 'https://www.sulpak.kz/f/otparivateli', 
             'Гладильные доски':'https://www.sulpak.kz/f/gladilniye_doski'}

def parse_category(category_name,category_link):
    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    driver.maximize_window()
    driver.get(category_link)
    button_close = driver.find_element(By.XPATH, "//*[@id='popup_city_default']/div[1]/div/div/div/div[3]/a[2]")
    button_close.click()

    qty_of_all_products = driver.find_element(By.XPATH, '//div[@class = "title__block-info"]').text.strip().replace(' товаров', '')
    qty_per_page = driver.find_elements(By.XPATH, "//div[@class='product__item product__item-js tile-container']")
    qty_page = math.ceil(int(qty_of_all_products)/(len(qty_per_page)-2))
    print('\n Количество страниц',qty_page, '\n')
    
    df = []
    for i in range(1, qty_page+1):
        new_url = category_link + '?page=' + str(i)
        print('\n', new_url, '\n')
        driver.get(new_url)
        soup = BeautifulSoup(driver.page_source)
        products = soup.find_all('div', class_="product__item product__item-js tile-container")
        for i in products:    
            title = i.find('div', class_ = 'product__item-name').text.strip()
            try:
                price1 = i.find('div',class_ = 'product__item-price').text.strip().replace('\xa0', '').replace('₸', '').replace(' ', '')
                try:
                    price2 = i.find('div',class_ = 'product__item-price-old').text.strip().replace('\xa0', '').replace('₸', '').replace(' ', '')
                except:
                    price2 = price1
            except:
                price1 = 0
                price2 = price1
            row = {'Time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'Title': title, 'Price with discount': price1, 'Actual price': price2}    
            print(row)
            df.append(row)
    data = pd.DataFrame(data = df)
    data['Price with discount'] = data['Price with discount'].astype(int)
    data['Actual price'] = data['Actual price'].astype(int)
    data['Discount(%)'] = round((data['Price with discount']/data['Actual price'] - 1)*100, 2)
    driver.close()
    data.to_csv('C:/Users/nsyrymbet/Desktop/test_parsing/'+str(category_name)+'.csv', encoding='utf-8-sig', index = False)
    
    
for k,v in categorys.items():
    print('Категория:', k, '\nСсылка:', v)
    parse_category(k,v)
