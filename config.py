from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions


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

        # headless/remote mode settings
        headless_options = ChromeOptions()
        headless_options.add_argument(f"--window-size={width},{height}")
        headless_options.headless = True

        # remote url
        #REMOTE_URL = "http://localhost:4444/wd/hub"
        REMOTE_URL = "http://selenium__standalone-chrome:4444/wd/hub"

        # Chrome window size settings
        chrome_window_size_options = ChromeOptions()
        chrome_window_size_options.add_argument(f"--window-size={width},{height}")

        # Firefox window size settings
        firefox_window_size_options = FirefoxOptions()
        firefox_window_size_options.add_argument(f"--width={width}")
        firefox_window_size_options.add_argument(f"--height={height}")

        self.browser = {
            "chrome": [webdriver.Chrome, chrome_window_size_options],
            "firefox": [webdriver.Firefox, firefox_window_size_options],
            "remote": [webdriver.Remote, REMOTE_URL, headless_options],
            "headless": [webdriver.Chrome, headless_options]
        }[BROWSER]

# sudo apt install openjdk-11-jre-headless
# java -jar selenium-server-4.1.3.jar standalone
