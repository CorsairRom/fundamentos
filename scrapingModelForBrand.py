import requests
from bs4 import BeautifulSoup
import os
import json
import re
from os import system

system("cls")

def get_data_model_by_brand(url):
    
    data_dict_exit = [{}]
    
    path_folder = 'pruebas\img-model'
    pattern = re.compile('var filter_data = (.*?);')
    
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    req = requests.get(url, headers=headers)
    print(req.status_code)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    scripts = soup.find_all('script')
    res = pattern.findall(str(scripts))
    
    for r in res:
        json_res = json.loads(r)
        
    for key in json_res.keys():
        try:
            nicknames = json_res[key]['nickname']
            volume_range = json_res[key]['volume_range']
            year_range = json_res[key]['year_range']
                
            for year in year_range:
                if 'до' in year:
                    min_year = int(year.split(' ')[-1])
                    # print(max_year)
                else:
                    min_year, max_year = map(int, year.split('...'))
                    # print(min_year, max_year)
                    
            for volume in volume_range:
                if 'от' in volume:
                    max_volume = int(volume.split(' ')[-1])
                    min_volume = 0
                else:
                    min_volume, max_volume = map(int, volume.split('...'))      
        except:
            nicknames = 'no-name'
            volume_range = 'no-volume-range'
            year_range = 0
            min_year = 0
            min_volume = 0  
        if min_year >= 2001:
            if max_volume > 600:
                data_bike_brand_model = {}       
                data_bike_brand_model['key_model'] = key
                data_bike_brand_model['nicknames'] = nicknames
                data_bike_brand_model['volume_range'] = volume_range
                data_bike_brand_model['year_range'] = year_range
                data_dict_exit.append(data_bike_brand_model)
            
    data_dict_exit[0]={'url': url}
    for data in data_dict_exit:
        print(data)  
        
get_data_model_by_brand('https://www.megazip.net/zapchasti-dlya-motocyklov/honda')