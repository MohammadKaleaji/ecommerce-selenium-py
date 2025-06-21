from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.NAME, "name")
    SEARCH_BUTTON = (By.CLASS_NAME, "search_button")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='shop-cart'] span.navbar-tool-label")
    PROFILE_ICON = (By.XPATH, "/html/body/header/div[2]/div[1]/div/div[2]/div[3]/a/div/div")
    LOGIN_LINK = (By.XPATH, "/html/body/header/div[2]/div[1]/div/div[2]/div[3]/div/a[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate("/")

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_cart_count(self):
        count_text = self.get_text(self.CART_ICON)
        return int(count_text) if count_text.isdigit() else 0

    def navigate_to_login(self):
        # Hover on the profile icon
        profile_icon = self.find_element(self.PROFILE_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(profile_icon).perform()

        # Wait for the login link to become clickable
        self.click(self.LOGIN_LINK)
