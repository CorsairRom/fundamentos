import requests
from bs4 import BeautifulSoup




def if_contains_more_model(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    req = requests.get(url, headers=headers)
    print('Response constains more model',req.status_code)
    soup = BeautifulSoup(req.text, 'html.parser')

    # IfExist = soup.find('div', 'sliding')
    IfExist = bool(soup.select('div.sliding'))

    return IfExist
    
if __name__ == '__main__':
    if_contains_more_model()