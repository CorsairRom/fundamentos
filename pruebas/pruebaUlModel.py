import requests
from bs4 import BeautifulSoup
import os
import json
import re
from os import system
import pruebaIfmoreModel

system('cls')

url = 'https://www.megazip.net/zapchasti-dlya-motocyklov/kawasaki'
path_folder = 'pruebas\img-model'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
req = requests.get(url, headers=headers)
print(req.status_code)
soup = BeautifulSoup(req.text, 'html.parser')
ulData = soup.find('ul', class_='s-catalog__columns-list').find_all('li')
# print(ulData)

for data in ulData:
    nameModel = data.find('a').text
    hrefModel = 'https://www.megazip.net' + data.find('a').get('href')
    extensible = pruebaIfmoreModel.if_contains_more_model(hrefModel)
    print(nameModel)
    print(hrefModel)
    print(extensible)
    

