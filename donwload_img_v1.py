import requests
import os
url = 'https://storage.megazip.net/catalog/S/20a/20adcd2963fd6db1f226cde35b40da41.png'
url2 = 'https://www.megazip.net/zapchasti-dlya-motocyklov/suzuki/gsx-r750-2301/gsx-r750-13989/gsx-r750k7-e3-e28-k7-768039'
url_text = url2.split('/')[-1]
print(url_text)
path=str('C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/'+url_text)
isExist = os.path.exists(path)
print(isExist)
if not isExist:
   # Create a new directory because it does not exist
   pr= os.makedirs(path)


name_img = url.split('/')[-1]

img_data = requests.get(url).content
img_rute = f'C:\/Web\/python\/webscraping\/fundamentos\/img-catalog\/{url_text}\/{name_img}'
img_exist = os.path.exists(img_rute)
if not img_exist:
    with open(img_rute, mode='wb') as handler:
        handler.write(img_data)
else:
    print('img exist')