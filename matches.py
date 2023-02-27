#Xpath //tagname[@attributename = 'value']

# Importing libraries
import os
import time
import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

print(selenium.__version__)
#To make sure the browser does not close after automation
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Opens browser and goes to the link, and maximizes the browser
driver.get("https://www.adamchoi.co.uk/overs/detailed")
driver.maximize_window()

#Clicking the All matches button on the site
all_matches_button = driver.find_elements("xpath", '//label[@analytics-event = "All matches"]')
all_matches_button[0].click()

#Finding the tagname for the data for scrapping
matches = driver.find_elements(By.TAG_NAME,'tr')

#Creating a list for the scrapped data
date = []
home_team = []
result = []
away_team = []


#Loop for selecting the individual scrapped data into respective list
for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text) 
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    result.append(match.find_element(By.XPATH, './td[3]').text)
    away = match.find_element(By.XPATH, './td[4]').text
    away_team.append(away)
    print(away)

#Quitting the site
driver.quit()


#Creating a dataframe and saving the scrapped data in it
df = pd.DataFrame({'date': date, 'home': home_team, 'result': result, 'away': away_team})
df.to_csv('matches.csv',index=False)
print(df)