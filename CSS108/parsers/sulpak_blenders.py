import requests
from bs4 import BeautifulSoup
HOST = 'https://www.sulpak.kz/'
URL = 'https://www.sulpak.kz/f/blenderiy'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

cards = []

def get_html(url,params=''):
    r = requests.get(url,headers=HEADERS,params=params,verify=False)
    return r 

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div',class_="goods-tiles")

    for item in items:
        cards.append({
            'title':item.find('div',class_="product-container-right-side").find('h3').get_text(strip=True),
            'price':item.find('div',class_="price").get_text(strip=True)
            
                
        })
    return cards
html = get_html(URL).text
import pandas as pd
df = pd.DataFrame(data = cards, columns = ["title", "price"])
df.to_csv(r'C:\Users\nsyrymbet\Desktop\internship Nuray\testing python\test.csv', encoding='utf-8-sig', index = False)
