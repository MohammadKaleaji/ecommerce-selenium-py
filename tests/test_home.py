import pytest
from pages.home_page import HomePage

def test_search_product(driver):
    home = HomePage(driver)
    home.search_product("حاسوب")  # Try searching for a word

def test_cart_icon(driver):
    home = HomePage(driver)
    count = home.get_cart_count()
    print(f"Cart Count: {count}")
    assert isinstance(count, int)

def test_navigate_to_login(driver):
    home = HomePage(driver)
    home.navigate_to_login()
    assert "login" in driver.current_url or "auth" in driver.current_url
