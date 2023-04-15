import requests
from bs4 import BeautifulSoup
from os import system

system("cls")

# estructura de datos a llegar

catalogo = [
    {
    "name_part":"",
    "url_img":"",
    "url_redirect":"",
    },
    {
        
    }
]


dic2 = [{}]



url = 'https://www.megazip.net/zapchasti-dlya-motocyklov/suzuki/gsx-r750-2301/gsx-r750-13989/gsx-r750k7-e3-e28-k7-768039'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
res = requests.get(url, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.title.text)
# print(dir(soup))
# .strip() elimina los saltos de linea los espacio en blanco los retornos de carro etc
clase = soup.find('ul', class_='part-group').find_all(class_='part-group__item')

count = []
part_finds = []


for part in clase:
    dic= {}
    url_scra = part.find('a').attrs['href']
    name_tex = part.find_all('a')[1].text
    # print(name_tex)
    img_scra = part.find('img').attrs['src']
    # print(img_scra)
    dic['nombre'] = name_tex
    dic['img'] = img_scra
    dic['href'] = 'https://www.megazip.net' + url_scra
    dic2.append(dic)
    # dic2.append(name_tex)
    # dic2.append(img_scra)
    # dic2.append(url_scra)
    
    
    # print(p)
#     part_finds.append(part)
dic2[0]={'url': url}
# print(dic2)
for d in dic2:
    print(d)


# print(part_finds[0])
# print('------------------')
# print(part_finds[8])




# for lsid in clase:
#     attr_id = lsid.attrs['id'].split('-')[2]
#     count.append(attr_id)
#     # print(attr_id)
# # print(len(count))
# print(clase)