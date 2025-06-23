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
    Base class for all page objects.
    Provides navigation, interaction, and browser setup.
    """

    def __init__(self, driver=None):
        self.driver = driver or self._init_driver()

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        # Uncomment for headless mode
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
        """Navigate to a full or relative URL."""
        if url.startswith("http"):
            full_url = url
        else:
            full_url = Environment.base_url().rstrip("/") + "/" + url.lstrip("/")
        self.driver.get(full_url)
        logging.info(f"Navigated to: {self.driver.current_url}")

    def _wait(self, condition, timeout=None):
        """Generic wait method."""
        return WebDriverWait(self.driver, timeout or Environment.ELEMENT_TIMEOUT).until(condition)

    def find_element(self, locator, timeout=None):
        """Find element by locator."""
        return self._wait(EC.presence_of_element_located(locator), timeout)

    def click(self, locator, timeout=None):
        """Click element by locator."""
        element = self._wait(EC.element_to_be_clickable(locator), timeout)
        element.click()

    def send_keys(self, locator, text, timeout=None):
        """Send keys to input field."""
        element = self._wait(EC.visibility_of_element_located(locator), timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        """Get visible text from element."""
        element = self.find_element(locator, timeout)
        return element.text.strip()

    def is_visible(self, locator, timeout=None):
        """Return True if element is visible."""
        try:
            self._wait(EC.visibility_of_element_located(locator), timeout)
            return True
        except:
            return False

    def get_page_source(self):
        """Return full HTML source of the current page."""
        return self.driver.page_source

    def quit(self):
        """Quit WebDriver instance."""
        if self.driver:
            self.driver.quit()
            logging.info("Chrome driver quit.")
