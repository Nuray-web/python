#В файле дан результат работы команды ping, Вам необходимо подсчитать среднее, минимальное и максимальное время ответа сервера. 
#Все числа необходимо округлить до целого и записать через пробел в следующем порядке: минимальное, среднее, максимальное.


import requests, re
from statistics import mean
url = 'https://raw.githubusercontent.com/bykov-alexei/data-science-course/master/%D0%92%D1%85%D0%BE%D0%B4%D0%BD%D0%BE%D0%B5%20%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/ping.txt'
r = requests.get(url).text
time_data = re.findall('время=\d{1,4}мс', r)
time_data = {int(x.replace('время=', '').replace('мс', '')) for x in time_data}
print(min(time_data), mean(time_data), max(time_data))
