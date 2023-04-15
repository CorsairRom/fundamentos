import requests
from bs4 import BeautifulSoup
import os

def data_bike_by_url(url):
    # initialize dictionary
    dic_exit = [{}]
    #config headers
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    # print url
    print(f'making the request to the url: {url}')
    # handle the exception in case the response takes longer
    try:
        req = requests.get(url, headers=headers, timeout=20)
        # stop execution and report error
        if req.status_code != 200:
            return {'Error': f'{req.reason}', 'status_code': f'{req.status_code}'}
    except:
        return {'Error': f'Error getting request from url: {url}'}
    # extract name of the catalog
    url_short = url.split('/')[-1]
    # create path for folder with catalog name
    path=str('C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/'+url_short)
    # ask if this path exists
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        new_dir= os.makedirs(path)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    # find catalog items
    data_ul_bike = soup.find('ul', class_='part-group').find_all(class_='part-group__item')
    
    # consult data for each item
    for li in data_ul_bike:
        # initial internal dict
        dic_init= {}
        # variables explain the steps
        part_name = li.find_all('a')[1].text
        part_redirect = li.find('a').attrs['href']
        part_img_src = li.find('img').attrs['src']
        # extract data img content 
        img_data = requests.get(part_img_src).content
        # create img name
        name_img = part_img_src.split('/')[-1]
        # create img route
        img_rute = f'C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/{url_short}\/{name_img}'
        # consult if img route already exist
        img_exist = os.path.exists(img_rute)
        if not img_exist:
            with open(img_rute, mode='wb') as handler:
                handler.write(img_data)
        else:
            print('img exist')
        # create dictionary
        dic_init['part_name'] = part_name
        dic_init['part_redirect'] = part_redirect
        dic_init['part_img_src'] = part_img_src
        # add data to external dictionary
        dic_exit.append(dic_init)
    # add url as first element of dictionary     
    dic_exit[0]={'url': url}
    
    return dic_exit

if __name__ == '__main__':
    data_bike_by_url()

