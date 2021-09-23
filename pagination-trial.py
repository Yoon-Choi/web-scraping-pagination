#https://en.zalando.de/premium-men-clothing/?p=2
#https://en.zalando.de/premium-men-clothing
# brand, product, price

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# useragent and request from webpage
hdr = {
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/92.0.4515.159Safari/537.36'}
html = requests.get('https://en.zalando.de/premium-men-clothing', headers=hdr)

# response checking
print("webpage response : ", html.status_code)

# pagination : this website is consist of 91 pages
search_result = []
for x in range(1, 91):
    url = 'https://en.zalando.de/premium-men-clothing/?p='
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('div', class_="_0xLoFW _78xIQ- EJ4MLB JT3_zV")
    print(content)
    for property in content:
        brand = property.find('span', class_='u-6V88 ka2E9k uMhVZi FxZV-M Kq1JPK pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2').text
        product = property.find('h3', class_='u-6V88 ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2').text
        price = property.find('span', class_='u-6V88 ka2E9k uMhVZi FxZV-M _6yVObe pVrzNP cMfkVL').text

        property_info = {
            'brand': brand,
            'product': product,
            'price': price
            }
        search_result.append(property_info)
print('search_result found : ', len(search_result))
time.sleep(3)
df = pd.DataFrame(search_result)
print(df.head())
df.to_csv('search_result.csv')