# config/config.py
import os

class Environment:
    # Environment selection (dev/staging/prod)
    CURRENT_ENV = os.getenv("APP_ENV", "staging")
    
    # Base URLs
    BASE_URLS = {
        "dev": "https://dev.your-ecom-site.com",
        "staging": "https://awisapp.com/",       #actually its production of the awis app 
        "prod": "https://www.your-ecom-site.com"
    }
    
    # Timeouts
    ELEMENT_TIMEOUT = int(os.getenv("ELEMENT_TIMEOUT", 15))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", 30))
    
    # Browser configuration
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    
    # Get current base URL
    @classmethod
    def base_url(cls):
        return cls.BASE_URLS[cls.CURRENT_ENV]

# Test data configuration
class TestData:
    SEARCH_TERMS = ["laptop", "wireless headphones", "running shoes"]
    PROMO_CODES = {"VALID": "WELCOME10", "INVALID": "EXPIRED2023"}

if __name__ == "__main__":
    print(f"Current Environment: {Environment.CURRENT_ENV}")
    print(f"Base URL: {Environment.base_url()}")
    print(f"Element Timeout: {Environment.ELEMENT_TIMEOUT}s")