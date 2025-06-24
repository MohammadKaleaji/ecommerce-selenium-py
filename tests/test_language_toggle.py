#tests/test_language_toggle.py
# test_language_toggle.py

import pytest
from pages.language_page import LanguagePage
from config.config import Environment

class TestLanguageToggle:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.page = LanguagePage(driver)

    def test_switch_to_arabic(self):
        print("\n[TEST] Switching to Arabic")
        self.driver.get(Environment.base_url())  # ✅ Ensure page is loaded
        self.page.switch_to_arabic()

    def test_switch_to_english(self):
        print("\n[TEST] Switching to English")
        self.driver.get(Environment.base_url())  # ✅ Ensure page is loaded
        self.page.switch_to_english()


