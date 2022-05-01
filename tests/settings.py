from envparse import env

"""
DIRECTORIES
"""
SCREENSHOT_DIR = env.str("SCREENSHOTS_DIR")
JUNIT_DIR = env.str("JUNIT_DIR")

"""
URLS
"""
SELENIUM_URL = "http://172.19.0.2:4444"
PROD_URL = "http://rozhkovqa.tilda.ws/test_form"
DEV_URL = "http://rozhkovqa.tilda.ws/test_form"