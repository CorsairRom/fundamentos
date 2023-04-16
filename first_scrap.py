import requests
from bs4 import BeautifulSoup
import os
from os import system

system("cls")



dic2 = [{}]



url = 'https://www.megazip.net/zapchasti-dlya-motocyklov/suzuki/gsx-r750-2301/gsx-r750-13989/gsx-r750k7-e3-e28-k7-768039'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
res = requests.get(url, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
clase = soup.find('ul', class_='part-group').find_all(class_='part-group__item')
print(clase.find('script'))
count = []
part_finds = []


for part in clase:
    dic= {}
    url_scra = part.find('a').attrs['href']
    name_tex = part.find_all('a')[1].text
    img_scra = part.find('img').attrs['src']

    dic['nombre'] = name_tex
    dic['img'] = img_scra
    dic['href'] = 'https://www.megazip.net' + url_scra
    dic2.append(dic)
 
    
    
    # print(p)
#     part_finds.append(part)
dic2[0]={'url': url}
print(dic2)
# for d in dic2:
#     print(d)

