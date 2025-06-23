# tests/test_search.py
import pytest
from pages.search_page import SearchPage

class TestSearch:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.search_page = SearchPage(driver)
        self.search_page.navigate("/")  # Explicitly navigate to homepage

    def test_search_valid_product(self):
        term = "مطارة شاي وقهوة نوعية ممتازة"
        print(f"\n[TEST] Searching for: {term}")
        self.search_page.search(term)
        assert self.search_page.has_results(), f"Expected results for term: {term}"

    def test_search_invalid_product(self):
        term = "laptop"
        print(f"\n[TEST] Searching for: {term}")
        self.search_page.search(term)
        assert self.search_page.has_no_results(), f"Expected no results for term: {term}"

    def test_search_with_empty_input(self):
        print("\n[TEST] Searching with empty input")
        self.search_page.search("")
        assert self.search_page.has_results(), "Expected results to appear when searching with empty input"
