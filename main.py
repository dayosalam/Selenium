import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#os.environ['PATH'] += r'C:\selenachium drivers'

#To make sure the browser does not close after automation
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#Opens browser and goes to the link, and maximizes the browser
driver.get("https://www.neuralnine.com")
driver.maximize_window()

#Finds all the href links and clicks on the books tab
links = driver.find_elements('xpath', "//a[@href]")
for link in links:
    if "Books" in link.get_attribute('innerHTML'):
        link.click()
        break

#Gets the link to a particular book 
book_links = driver.find_elements('xpath', "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a" )

# Clicks on the link
book_links[0].click()

# Switching to the next tab 
driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

# Getting t
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print(button.get_attribute('innerHTML'))


