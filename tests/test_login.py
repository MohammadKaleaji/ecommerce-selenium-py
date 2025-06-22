# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.credentials import CredentialManager

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)

    def test_valid_login(self):
        print("\n🧪 Running test: Valid Login")
        self.login_page.login_with_valid_credentials()
        assert "account" in self.home_page.driver.current_url or "الرئيسية" in self.home_page.get_page_source()

    @pytest.mark.parametrize("email, password", [
        ("invalid@test.com", "wrongpass"),
        ("", "somepass"),
        ("valid@email.com", ""),
        ("", ""),
    ])
    def test_invalid_logins(self, email, password):
        print(f"\n🧪 Running test: Invalid Login with email='{email}' and password='{password}'")
        self.login_page.login(email, password)
        assert "/auth/login" in self.login_page.driver.current_url or "خطأ" in self.login_page.get_page_source()