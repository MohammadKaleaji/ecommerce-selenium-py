# pages/login_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import CredentialManager

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "si-email")
    PASSWORD_INPUT = (By.ID, "si-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.delete_all_cookies()  # Ensure a fresh session
        self.navigate("/customer/auth/login")
        # Wait for the login form to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )

    def login(self, email, password):
        print(f"[INFO] Logging in with {email}")
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def login_with_valid_credentials(self):
        creds = CredentialManager.get_credentials()
        self.login(creds["username"], creds["password"])

    def get_page_source(self):
        return self.driver.page_source