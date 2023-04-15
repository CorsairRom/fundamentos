import requests
from bs4 import BeautifulSoup
import os

def data_bike_by_url(url):
    #initialize dictionary
    dic_exit = [{}]
    #config headers
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    print(f'making the request to the url: {url}')
    try:
        req = requests.get(url, headers=headers, timeout=20)
        if req.status_code != 200:
            return {'Error': f'{req.reason}', 'status_code': f'{req.status_code}'}
    except:
        return {'Error': f'Error getting request from url: {url}'}
    url_short = url.split('/')[-1]
    path=str('C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/'+url_short)
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        new_dir= os.makedirs(path)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    data_ul_bike = soup.find('ul', class_='part-group').find_all(class_='part-group__item')
    
    for li in data_ul_bike:
        dic_init= {}
        part_name = li.find_all('a')[1].text
        part_redirect = li.find('a').attrs['href']
        part_img_src = li.find('img').attrs['src']
        img_data = requests.get(part_img_src).content
        name_img = part_img_src.split('/')[-1]
        img_rute = f'C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/{url_short}\/{name_img}'
        img_exist = os.path.exists(img_rute)
        if not img_exist:
            with open(img_rute, mode='wb') as handler:
                handler.write(img_data)
        else:
            print('img exist')
        
        dic_init['part_name'] = part_name
        dic_init['part_redirect'] = part_redirect
        dic_init['part_img_src'] = part_img_src
        dic_exit.append(dic_init)
        
    dic_exit[0]={'url': url}
    
    return dic_exit

pru = data_bike_by_url('https://www.megazip.net/zapchasti-dlya-motocyklov/suzuki/gsx-r750-2301/gsx-r750-13989/gsx-r750u2k8-e2-k8-768043')
print(pru)