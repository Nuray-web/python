from bs4 import BeautifulSoup  # для парсинга старниц
import requests                # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random

url = 'https://kolesa.kz/cars/almaty/?page='
cars = []
count = 1
while count <= 2:
    url = 'https://kolesa.kz/cars/almaty/?page=' + str(count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    car_data = html_soup.find_all('div', class_="row vw-item list-item a-elem")
    if car_data != []:
        cars.extend(car_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1
    
print(len(cars))
print(cars[1])
print()
n = int(len(cars)) - 1
count = 0
while count <= 5:  # count <= n
    info = cars[int(count)]
    price = info.find('span',{"class":"price"}).text
    title = info.find('span',{"class":"a-el-info-title"}).text
    print('\n', title, ' ', price, '\n')
    count += 1
