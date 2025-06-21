# tests/test_home.py
from pages.home_page import HomePage

def test_search_product(driver):
    print("\n🔍 [TEST] Running: Search for a product")
    home = HomePage(driver)
    home.search_product("قلاية")

def test_get_cart_count(driver):
    print("\n🛒 [TEST] Running: Get cart item count")
    home = HomePage(driver)
    cart_count = home.get_cart_count()
    print(f"Cart Count: {cart_count}")

def test_navigate_to_login(driver):
    print("\n🔐 [TEST] Running: Navigate to login page")
    home = HomePage(driver)
    home.navigate_to_login()
