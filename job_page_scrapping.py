
import csv
import requests
from bs4 import BeautifulSoup

# import pandas as pd
# import time

# useragent and request for webpage
hdr = {
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/92.0.4515.159Safari/537.36'}
html = requests.get(
    ' https://www.glassdoor.com/Job/berlin-junior-data-analyst-jobs-SRCH_IL.0,6_IC2622109_KO7,26.htm?srs=JOBS_HOME_RECENT_SEARCHES',
    headers=hdr)

# response checking
print("webpage response : ", html.status_code)

page_soup = BeautifulSoup(html.content, 'lxml')

company_name = []
position_name = []
location_name = []
job_age = []

containers = page_soup.find_all('div', {'class': "d-flex flex-column pl-sm css-1d3xmk8 e1rrn5ka4"})
for container in containers:
    # company-name extraction
    for company in container.find_all('div', {'class': "d-flex justify-content-between align-items-start"}):
        temp = company.a.span.text
        company_name.append(temp)

    # position extraction
    for position in container.find_all("a", {"class": "jobLink css-1rd3saf eigr9kq2"}):
        temp = position.text
        position_name.append(temp)

    # location
    for location in container.find_all("span", {"class": "pr-xxsm css-1ndif2q e1rrn5ka0"}):
        location_name.append(location.text)

    # job age (uploaded date)
    for jobage in container.find_all("div", {"class": "d-flex align-items-end pl-std css-mi55ob"}):
        job_age.append(jobage.text)

# ## checking results
# # company
# print("company name : ", company_name)
# print("length of list : ", len(company_name))
# #
# # position
# print("\nposition : ", position_name)
# print("length of list : ", len(position_name))
#
# # location name
# print("\nlocation name : ", location_name)
# print("length of list : ", len(location_name))
# # job age
# print("\njob age : ", job_age)
# print("length of list : ", len(job_age))
#
# # checking consistency
# print('\n\n"consistency checking"')
# print(company_name[3], '\n', position_name[3], '\n', location_name[3], '\n', job_age[3])

## write data : csv
with open('job-list.csv', mode='w', encoding='utf8') as myfile:
    wr = csv.writer(myfile)
    for data in range(len(company_name)):
        wr.writerow([company_name[data], position_name[data], location_name[data], job_age[data]])
