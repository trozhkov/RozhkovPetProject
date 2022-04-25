from selenium import webdriver


class Config:
    def __init__(self, configuration):

        ENV = configuration["env"]
        BROWSER = configuration["browser"]

        # Choose URL and port
        SUPPORTED_ENVS = ["prod", "dev"]

        if ENV.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{ENV} is not supported (supported environments: {SUPPORTED_ENVS})")

        self.base_url = {
            "prod": "http://rozhkovqa.tilda.ws/test_form",
            "dev": "http://rozhkovqa.tilda.ws/test_form",
        }[ENV]

        self.app_port = {
            "prod": 8080,
            "dev": 8080,
        }[ENV]

        # Choose browser
        SUPPORTED_BROWSERS = ["chrome", "firefox", "remote", "headless"]

        if BROWSER.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f"{BROWSER} is not supported (supported browsers: {SUPPORTED_BROWSERS})")

        self.base_browser = {
            "chrome": webdriver.Chrome,
            "firefox": webdriver.Firefox,
            "remote": webdriver.Remote,
            #"headless": webdriver.Chrome(options=Options().add_argument("--headless"))
        }[BROWSER]
