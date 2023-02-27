from selenium import webdriver

website = "https://www.adamchoi.co.uk/overs/detailed"
path = '/Users/i/Downloads/Compressed/chromedriver_win32_1'
driver = webdriver.Chrome(path)
driver.get(website)

driver.maximize_window()

all_matches_button = driver.find_elements("xpath", '//label[@analytics-event = "All matches"]')
all_matches_button[0].click()

matches = driver.find_elements("tagname",'tr')

for match in matches:
    print(match.text)