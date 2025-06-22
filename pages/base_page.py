# pages/base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Environment
import logging
import os

class BasePage:
    """
    Simplified base class for all page objects.
    Chrome-only, with essential Selenium actions.
    """

    def __init__(self, driver=None):
        self.driver = driver or self._init_driver()

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # Add a custom user-agent to help avoid Selenium detection
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        # Uncomment the next line if you want to run headless
        # chrome_options.add_argument("--headless=new")

        driver_path = os.getenv("CHROME_DRIVER_PATH", "drivers/chromedriver")
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.set_page_load_timeout(Environment.PAGE_LOAD_TIMEOUT)
        driver.implicitly_wait(Environment.ELEMENT_TIMEOUT)
        driver.maximize_window()

        logging.info("Chrome driver initialized.")
        return driver

    def navigate(self, url):
        """Navigate to a full or relative URL, ensuring no double slashes."""
        if url.startswith("http"):
            full_url = url
        else:
            # Remove trailing slash from base_url and leading slash from url
            full_url = Environment.base_url().rstrip("/") + "/" + url.lstrip("/")
        self.driver.get(full_url)
        logging.info(f"Navigated to: {self.driver.current_url}")

    def find_element(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or Environment.ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=None):
        element = WebDriverWait(self.driver, timeout or Environment.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def send_keys(self, locator, text, timeout=None):
        element = WebDriverWait(self.driver, timeout or Environment.ELEMENT_TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        return self.find_element(locator, timeout).text

    def is_visible(self, locator, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or Environment.ELEMENT_TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_page_source(self):
        return self.driver.page_source

    def quit(self):
        if self.driver:
            self.driver.quit()
            logging.info("Chrome driver quit.")