from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time
import pandas as pd
number_of_pages = 664

row = []
website = "https://www.bayut.sa/en/for-sale/properties/ksa/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(website)
time.sleep(5)

for page in range(number_of_pages):
    try:
        element = driver.find_element(By.XPATH, '//ul')

            # get children of tag 'ul' with tag 'li'
        elements  = driver.find_elements(By.XPATH, './/li')
        for e in elements:
            text = e.text
            lines = text.split('\n')
            if len(lines) == 11:
                row.append([lines[1],lines[2],lines[3],lines[4],lines[6],lines[8]])
            elif len(lines) == 12:
                row.append([lines[2],lines[3],lines[4],lines[5],lines[7],lines[9]])
        time.sleep(2)
        driver.get(f'https://www.bayut.sa/en/for-sale/properties/ksa/page-{page+2}/')
    except:
        df= pd.DataFrame(row,columns=['Price', 'Property Type', 'Number Of Bedrooms', 'Number Of Bathrooms', 'Area', 'Location'])
    finally:
        df= pd.DataFrame(row,columns=['Price', 'Property Type', 'Number Of Bedrooms', 'Number Of Bathrooms', 'Area', 'Location'])
        # df.to_csv('bayut_listings.csv', index=False)


print(df)
