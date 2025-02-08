from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Corrected ChromeDriver path (including 'chromedriver.exe')
path = r'C:\chromedriver-win64\chromedriver.exe'

# URL to open
website = 'https://nepsealpha.com/traded-stocks'

# Use Service to initialize WebDriver
driver = webdriver.Chrome(service=Service(path))

# Open the website
driver.get(website)
