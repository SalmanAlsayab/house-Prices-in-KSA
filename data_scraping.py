from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time
import pandas as pd
number_of_pages = 664

row = []
website = "https://www.bayut.sa/en/for-sale/properties/ksa/"
arr = []
arr1 = []
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get(website)

element = driver.find_element(By.XPATH, '//ul')

    # get children of tag 'ul' with tag 'li'
elements  = driver.find_elements(By.XPATH, './/li')
count=0
links = driver.find_elements(By.TAG_NAME, 'a')
for e in elements:
    arr.append(e.text)

for i in range(len(arr)):
    lines = arr[i].split('\n')
    arr1.append(lines)

for i in arr1:
    if len(i) == 11:
        row.append([i[1],i[2],i[3],i[4],i[6],i[8]])
        print(row)
    elif len(i) == 12:
        row.append([i[2],i[3],i[4],i[5],i[7],i[9]])
time.sleep(2)

for i in range(number_of_pages-1):
    arr = []
    arr1 = []
    driver.get(f'https://www.bayut.sa/en/for-sale/properties/ksa/page-{i+2}/')

    element = driver.find_element(By.XPATH, '//ul')

        # get children of tag 'ul' with tag 'li'
    elements  = driver.find_elements(By.XPATH, './/li')
    links = driver.find_elements(By.TAG_NAME, 'a')
    for e in elements:
        arr.append(e.text)

    for i in range(len(arr)):
        lines = arr[i].split('\n')
        arr1.append(lines)

    for i in arr1:
        if len(i) == 11:
            row.append([i[1],i[2],i[3],i[4],i[6],i[8]])
        elif len(i) == 12:
            row.append([i[2],i[3],i[4],i[5],i[7],i[9]])
    time.sleep(2)
df= pd.DataFrame(row,columns=['Price', 'Property Type', 'Number Of Bedrooms', 'Number Of Bathrooms', 'Area', 'Location'])
df.to_csv('bayut_listings.csv', index=False)

print(df)
