from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.sulpak.kz/f/utyugi'
driver.get(url)

button_close = driver.find_element(By.XPATH, "//*[@id='popup_city_default']/div[1]/div/div/div/div[3]/a[2]")
button_close.click()

soup = BeautifulSoup(driver.page_source)
products = soup.find_all('div', class_="product__item product__item-js tile-container")

len(products)

data = []
rows = {}

for i in products:
    title = i.find()
