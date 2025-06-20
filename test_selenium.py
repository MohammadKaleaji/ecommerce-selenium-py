"""
# For Chrome:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

try:
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    print("Test passed for Chrome!")

except Exception as e:
    print(f"An error occurred with Chrome: {e}")

finally:
    if 'driver' in locals() and driver:
        time.sleep(3)
        driver.quit()
"""