import requests
from bs4 import BeautifulSoup
import os
import json
import re
from os import system

system('cls')

url = 'https://www.megazip.net/zapchasti-dlya-motocyklov/suzuki/gsx-r1000-2292/gsx-r1000-13980'
# url = 'https://www.megazip.net/zapchasti-dlya-motocyklov/kawasaki/zx1400-16032/zx1400-31583'
path_folder = 'pruebas\img-model'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
req = requests.get(url, headers=headers)
print(req.status_code)
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup)
ulVariants = soup.find('ul', 's-catalog__body-variants').find_all('div', 's-catalog__body-variants-item-content')

año = []
for variant in ulVariants:
    yearModel = int(variant.find('dd', 's-catalog__attrs-data').text.strip())
    if yearModel >=2000:
        if yearModel not in año:
            año.append(yearModel)
            attrsVarianModel = variant.find_all('dl', 's-catalog__attrs')
            print('año: ', yearModel)
            try:
                modelCC = int(variant.find('dt', text='Engine Capacity').find_next_sibling('dd').text.strip())
            except:
                modelCC = 0
            if modelCC >= 600:
                print('CC: ', modelCC)
                href = 'https://www.megazip.net'+variant.find('a', 's-catalog__body-variants-name').get('href')
                print('href: ',href)
