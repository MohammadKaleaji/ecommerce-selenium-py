# pages/search_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config import Environment

class SearchPage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-bar-input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search_button")
    
    # Result appears as anchor with /product/ in href
    RESULT_ITEMS = (By.XPATH, "//a[contains(@href, '/product/')]")
    NO_RESULTS = (By.XPATH, "//h6[contains(text(),'لم يتم العثور على المنتج')]")

    def search(self, term):
        """Enter a search term and trigger the search"""
        self.send_keys(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def has_results(self):
        """Check if search yielded any product links"""
        try:
            WebDriverWait(self.driver, Environment.ELEMENT_TIMEOUT).until(
                EC.presence_of_element_located(self.RESULT_ITEMS)
            )
            return True
        except:
            return False

    def has_no_results(self):
        """Check if 'no result' message is shown"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.NO_RESULTS)
            )
            return True
        except:
            return False
