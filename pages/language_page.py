#pages/language_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from config.config import Environment

class LanguagePage(BasePage):
    LANGUAGE_TOGGLE = (By.CSS_SELECTOR, "div.__language-bar > a.dropdown-toggle")
    ENGLISH_OPTION = (By.XPATH, "//li[@data-language-code='en']")
    ARABIC_OPTION = (By.XPATH, "//li[@data-language-code='ae']")

    def open_language_dropdown(self):
        WebDriverWait(self.driver, Environment.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(self.LANGUAGE_TOGGLE)
        ).click()

    def switch_to_english(self):
        self.open_language_dropdown()
        WebDriverWait(self.driver, Environment.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(self.ENGLISH_OPTION)
        ).click()

    def switch_to_arabic(self):
        self.open_language_dropdown()
        WebDriverWait(self.driver, Environment.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(self.ARABIC_OPTION)
        ).click()

