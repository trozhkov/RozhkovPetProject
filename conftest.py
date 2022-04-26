from pytest import fixture
from config import Config

"""
FIXTURES
"""


@fixture(scope="session")
def drv(app_config, get_parameters):
    """
    app_config.browser returns a list
    chrome, firefox, and headless keywords return a list with two items:
    webdriver object and options
    remote keyword returns a list with webdriver,
    selenium server url, and options
    """
    browser = app_config.browser[0]  # webdriver object

    if get_parameters["browser"] == "remote":
        exe_path = app_config.browser[1]  # remote server url
        ARGS = app_config.browser[2]  # options
        drv = browser(command_executor=exe_path,
                      options=ARGS)
    else:
        ARGS = app_config.browser[1]  # webdriver object
        drv = browser(options=ARGS)  # options

    yield drv

    drv.quit()


"""
ADD PARAMETERS
"""


def pytest_addoption(parser):
    """avoid adding on letter options like -g"""
    parser.addoption("--env",
                     action="store",
                     default="dev",
                     help="Specify environment")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Select browser")


@fixture(scope="session")
def get_parameters(request):
    """
    detects what keywords was used with an option.
    Ex: --env prod
    """
    config_param = {
        "env": request.config.getoption("--env"),
        "browser": request.config.getoption("--browser")
    }
    return config_param


@fixture(scope="session")
def app_config(get_parameters):
    """
    Returns value from a Config dictionary
    """
    configuration = Config(get_parameters)
    return configuration

# def make_screenshot(self, name=None):
#     test_name = self._test_fn_name
#
#     if name is None:
#         try:
#             index = self._screenshot_index
#         except AttributeError:
#             index = 1
#
#         self._screenshot_index = index + 1
#         name = str(index)
#
#     screenshot_name = f'{test_name}/{name}.png'
#     path_to_screenshot = os.path.abspath(os.path.join(SCREENSHOTS_DIR, screenshot_name))
#     screenshot_dir = os.path.dirname(path_to_screenshot)
#     os.makedirs(screenshot_dir, exist_ok=True)
#     self.save_screenshot(path_to_screenshot)

# test_name = request.function.__name__
# driver._test_fn_name = test_name
#
# yield driver
#
# try:
#     driver.make_screenshot('final')
# except:
#     pass
#
# driver.quit()
