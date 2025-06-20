# conftest.py
import pytest
from pages.base_page import BasePage
import logging
import os
from datetime import datetime

# Configure logging once for all tests
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@pytest.fixture(scope="function")
def driver(request):
    """Set up Chrome WebDriver and take screenshot on failure."""
    base = BasePage()
    driver = base.driver

    def teardown():
        # Capture screenshot if test failed
        if request.node.rep_call.failed:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{request.node.name}_{timestamp}.png"
            path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(path)
            logging.error(f"[FAIL] Screenshot saved: {path}")
        
        driver.quit()
        logging.info("[INFO] Driver quit")

    request.addfinalizer(teardown)
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Make test report available in fixture (e.g. for screenshots)."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
