# Import necessary libraries
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import service  # This import is not used
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Define the number of pages to scrape
number_of_pages = 664

# Initialize an empty list to store each row of data
row = []

# Target website URL
website = "https://www.bayut.sa/en/for-sale/properties/ksa/"

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open after script ends

# Start Chrome driver with the options
driver = webdriver.Chrome(options=options)

# Open the initial website
driver.get(website)
time.sleep(5)  # Wait for the page to fully load

try:
    # Loop through the specified number of pages
    for page in range(number_of_pages):
            # Locate the main <ul> element that contains the property listings
            element = driver.find_element(By.XPATH, '//ul')

            # Find all <li> elements inside the <ul> (individual listings)
            elements  = driver.find_elements(By.XPATH, './/li')

            # Process each listing element
            for e in elements:
                text = e.text
                lines = text.split('\n')  # Split the text by lines

                # Check the number of lines and extract relevant information accordingly
                if len(lines) == 11:
                    row.append([lines[1], lines[2], lines[3], lines[4], lines[6], lines[8]])
                elif len(lines) == 12:
                    row.append([lines[2], lines[3], lines[4], lines[5], lines[7], lines[9]])

            # Wait before navigating to the next page
            time.sleep(2)

            # Go to the next page
            driver.get(f'https://www.bayut.sa/en/for-sale/properties/ksa/page-{page+2}/')

except:
    # In case of an exception (e.g., elements not found), create a DataFrame from the collected rows so far
    df = pd.DataFrame(row, columns=['Price', 'Property Type', 'Number Of Bedrooms', 'Number Of Bathrooms', 'Area', 'Location'])

finally:
    # Ensure the DataFrame is created and file created at the end regardless of errors
    df = pd.DataFrame(row, columns=['Price', 'Property Type', 'Number Of Bedrooms', 'Number Of Bathrooms', 'Area', 'Location'])
    # Optional: Save to CSV
    df.to_csv('bayut_listings.csv', index=False)

# Print the final DataFrame
if __name__ == '__main__':
    print(df)
