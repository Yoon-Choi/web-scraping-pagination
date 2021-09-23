
#https://en.zalando.de/clothing/

# brand_name, product_name, price

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


search_result = []



for x in range(1, 3):  # pagination
    url = 'https://www.glassdoor.com/Job/berlin-junior-data-analyst-jobs-SRCH_IL.0,6_IC2622109_KO7,26.htm?includeNoSalaryJobs=true&p='
    r = requests.get(url+str(x)) # page넘겨가면서 html끝에 페이지번호가 보이는것을 확인 후에
    soup = BeautifulSoup(r.content, 'html.parser')
    content = soup.find_all('div', class_ =  "d-flex flex-column pl-sm css-1d3xmk8 e1rrn5ka4")
    print(content)
    for property in content:
        company = property.find('div', class_='d-flex justify-content-between align-items-start').text
        position = property.find('a', class_='jobLink css-1rd3saf eigr9kq2').text
        location = property.find('span', class_='pr-xxsm css-1ndif2q e1rrn5ka0').text
        job_age = property.find('div', class_='d-flex align-items-end pl-std css-mi55ob').text
        property_info = {
            'company' : company,
            'position': position,
            'location' : location,
            'job_age' : job_age}
        search_result.append(property_info)
print('search_result found : ', len(search_result))
time.sleep(3)
df = pd.DataFrame(search_result)
print(df.head())
df.to_csv('search_result.csv')