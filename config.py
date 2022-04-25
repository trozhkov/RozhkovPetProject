from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxOptions

class Config:
    def __init__(self, configuration):

        ENV = configuration["env"]
        BROWSER = configuration["browser"]

        # Choose URL and port
        SUPPORTED_ENVS = ["prod", "dev"]

        if ENV.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{ENV} is not supported (supported environments: {SUPPORTED_ENVS})")

        self.url = {
            "prod": "http://rozhkovqa.tilda.ws/test_form",
            "dev": "http://rozhkovqa.tilda.ws/test_form",
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

        # headless mode settings
        headless_options = Options()
        headless_options.headless = True

        # Chrome window size settings
        chrome_window_size_options = Options()
        chrome_window_size_options.add_argument(f"--window-size={width},{height}")

        # Firefox window size settings
        firefox_window_size_options = FirefoxOptions()
        firefox_window_size_options.add_argument(f"--width={width}")
        firefox_window_size_options.add_argument(f"--height={height}")

        self.browser = {
            "chrome": [webdriver.Chrome, chrome_window_size_options],
            "firefox": [webdriver.Firefox, firefox_window_size_options],
            "remote": [webdriver.Remote, None],
            "headless": [webdriver.Chrome, headless_options]
        }[BROWSER]
