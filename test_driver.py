from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("drivers/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
