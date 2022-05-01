import os
from tests import settings
import inspect


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._screenshot_index = 1

    def go(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def take_screenshot(self):
        # f_back outputs the name of the calling function
        test_name = inspect.currentframe().f_back.f_code.co_name

        # path to the test_name directory
        directory_path = os.path.abspath(
            os.path.join(settings.SCREENSHOT_DIR, f"{test_name}")
        )

        image_name = str(self._screenshot_index)
        screenshot_name = f"{test_name}/{image_name}.png"

        # join dir name and image name to create absolute path
        screenshot_path = os.path.abspath(
            os.path.join(
                settings.SCREENSHOT_DIR, screenshot_name)
        )

        # create test_name directory if it does not exist
        os.makedirs(directory_path,
                    exist_ok=True)  # create directory

        # save screenshot
        self.driver.save_screenshot(screenshot_path)
        self._screenshot_index += 1
