from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from tests import settings


class Config:
    def __init__(self, configuration):

        # assign configuration dict items to variables
        ENV = configuration["env"]
        BROWSER = configuration["browser"]

        # Choose URL and port
        SUPPORTED_ENVS = ["prod", "dev"]

        if ENV.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{ENV} is not supported (supported environments: {SUPPORTED_ENVS})")

        self.url = {
            "prod": settings.PROD_URL,
            "dev": settings.DEV_URL,
        }[ENV]

        self.port = {
            "prod": 8080,
            "dev": 8080,
        }[ENV]

        # Choose browser
        SUPPORTED_BROWSERS = ["chrome", "firefox", "remote", "headless"]

        if BROWSER.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f"{BROWSER} is not supported (supported browsers: {SUPPORTED_BROWSERS})")

        # window size parameters
        height = "1080"
        width = "1920"

        # headless/remote mode settings
        headless_options = webdriver.ChromeOptions()
        headless_options.add_argument(f"--window-size={width},{height}")
        headless_options.headless = True

        # Chrome settings
        chrome_service = Service(executable_path=ChromeDriverManager().install())
        chrome_window_size_options = webdriver.ChromeOptions()
        chrome_window_size_options.add_argument(f"--window-size={width},{height}")

        # Firefox settings
        firefox_service = Service(executable_path=GeckoDriverManager().install())
        firefox_window_size_options = webdriver.FirefoxOptions()
        firefox_window_size_options.add_argument(f"--width={width}")
        firefox_window_size_options.add_argument(f"--height={height}")

        self.browser = {
            "chrome": [webdriver.Chrome, chrome_window_size_options, chrome_service],
            "firefox": [webdriver.Firefox, firefox_window_size_options, firefox_service],
            "remote": [webdriver.Remote, settings.SELENIUM_URL, headless_options],
            "headless": [webdriver.Chrome, headless_options, chrome_service]
        }[BROWSER]
