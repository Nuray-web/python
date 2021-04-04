from bs4 import BeautifulSoup
import urllib.request
import time
import pandas as pd

url = 'https://kolesa.kz/cars/region-almatinskaya-oblast'
cars = []
count = 1
while count <= 1010:
    new_url = url+ '/?page=' + str(count)
    print(count)
    response = urllib.request.urlopen(new_url)
    html_soup = BeautifulSoup(response, 'html.parser')
    car_data = html_soup.find_all('div', class_="row vw-item list-item a-elem")
    yellow_data = html_soup.find_all('div', class_="row vw-item list-item yellow a-elem")
    blue_data = html_soup.find_all('div', class_="row vw-item list-item blue a-elem")
    cars.extend(car_data)
    cars.extend(yellow_data)
    cars.extend(blue_data)
    time.sleep(1)
    count += 1

carslist = []  
d = {}  
print('\n\n')
count = 0
print('---'*20)
while count <= 20005:
    print(count)
    info = cars[int(count)]
    price = info.find('span',class_="price").text.strip()
    title = info.find('span',class_="a-el-info-title").text.strip()
    extra = info.find('div',class_="a-search-description").text.strip()
    exurl = 'https://kolesa.kz' + (info.a.get('href'))
    print('The page of the advertisement:', exurl)
    respond = urllib.request.urlopen(exurl)
    html = BeautifulSoup(respond, 'html.parser')
    data = html.find('h1', class_="offer__title").text.strip()
    time.sleep(0.5)
    #desc = html.find('div', class_='text').text.strip()
    #print('\nНазвание данной машины:',title,'\nЦена:',price) #'\nОписание:',desc)
    car = {
        'Название' : title,
        'Цена' : price
        #'Объявление' : info.find('div',class_="a-search-description").text.strip()
    }
    for data in html.find_all("dl"):
        key = data.dt.text.strip()
        value = data.dd.text.strip()
        #print('{}: {}'.format(key,value))
        d[key] = value
        car.update(d)
    carslist.append(car)
    #print()
    #print('---'*20)
    count += 1

print('\n')
df = pd.DataFrame(data = carslist, columns = ['Название', 'Цена', 'Город', 'Кузов', 'Объем двигателя, л', 'Коробка передач', 'Руль', 'Цвет', 'Привод', 'Растаможен в Казахстане', 'Пробег', 'VIN', 'Наличие'])
df.to_csv(r'C:\Users\Win10\OneDrive\Документы\My projects\test2.csv', encoding='utf-8-sig', index = False)
print(df.head)
print('\n\n')

j = pd.read_csv(r'C:\Users\Win10\OneDrive\Документы\My projects\test2.csv')
print(j.head(5))
