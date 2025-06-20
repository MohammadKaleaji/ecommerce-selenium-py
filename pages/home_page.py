from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class HomePage(BasePage):
    # Updated locators
    SEARCH_INPUT = (By.CLASS_NAME, "search-bar-input")
    SEARCH_BUTTON = (By.CLASS_NAME, "search_button")

    CART_COUNT_SPAN = (By.CSS_SELECTOR, ".navbar-tool-icon-box .navbar-tool-label")

    PROFILE_ICON = (By.CSS_SELECTOR, ".navbar-tool-icon-box.bg-secondary")  # For hover
    LOGIN_LINK = (By.LINK_TEXT, "تسجيل الدخول")  # Arabic text of "Sign In"

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate("/")  # Goes to https://awisapp.com/

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_cart_count(self):
        text = self.get_text(self.CART_COUNT_SPAN)
        return int(text.strip()) if text.strip().isdigit() else 0

    def navigate_to_login(self):
        # Hover to show login link
        actions = ActionChains(self.driver)
        profile_icon = self.find_element(self.PROFILE_ICON)
        actions.move_to_element(profile_icon).perform()

        self.click(self.LOGIN_LINK)
