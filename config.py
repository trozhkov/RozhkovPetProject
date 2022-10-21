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
        MODE = configuration["mode"]

        # Choose URL and MAIL URL
        SUPPORTED_ENVS = ["stage", "prod", "local"]

        if ENV.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{ENV} is not supported (supported environments: {SUPPORTED_ENVS})")

        urls_dict = {
            "local": ""
        }

        mailhog_urls_dict = {
            "local": "settings.MY_BRANCH_MAILHOG_URL"
        }

        meta_admin_urls_dict = {
            "local": "settings.MY_BRANCH_META_URL"
        }

        self.url = urls_dict[ENV]

        self.mailhog_url = mailhog_urls_dict[ENV]

        self.meta_url = meta_admin_urls_dict[ENV]

        # Choose browser
        SUPPORTED_BROWSERS = ["chrome", "firefox", "remote", "headless"]

        if BROWSER.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f"{BROWSER} is not supported (supported browsers: {SUPPORTED_BROWSERS})")

        # window size parameters
        height = "1080"
        width = "1920"

        # headless/remote options
        headless_options = webdriver.ChromeOptions()
        headless_options.add_argument(f"--window-size={width},{height}")
        headless_options.headless = True

        # Chrome options
        chrome_service = Service(executable_path="./drivers/chromedriver")
        # chrome_service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--window-size={width},{height}")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option("detach", True)

        # Firefox settings
        firefox_service = Service(executable_path="./drivers/geckodriver")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument(f"--width={width}")
        firefox_options.add_argument(f"--height={height}")

        supported_browsers_dict = {
            "chrome": [webdriver.Chrome, chrome_options, chrome_service],
            "firefox": [webdriver.Firefox, firefox_options, firefox_service],
            "remote": [webdriver.Remote, settings.SELENIUM_URL, headless_options],
            "headless": [webdriver.Chrome, headless_options, chrome_service]
        }

        self.browser = supported_browsers_dict[BROWSER]

        # choose mode
        SUPPORTED_MODES = ["prod", "debug"]

        if MODE.lower() not in SUPPORTED_MODES:
            raise Exception(f"{MODE} is not supported (supported modes: {SUPPORTED_MODES})")
