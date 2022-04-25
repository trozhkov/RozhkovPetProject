from pytest import fixture
from config import Config

"""
FIXTURES
"""

# @pytest.fixture
# def drv(request):
#     """
#     SETUP DRIVER
#     * Is passed into driver.py in the form of Driver(driver_class), which is webdriver.Chrome()
#
#     MAKE SCREENSHOTS
#     * Assign screenshot index to the image incrementing by one with every new image,
#     the final image is called final
#     * Performed by driver.py make_screenshot()
#     """
#     driver = Driver(**driver_kwargs)
#
#     # try:
#     #     # Remove zendesk
#     #     zendesk = driver.find_element_by_css_selector('iframe#launcher')
#     #     driver.execute_script("arguments[0].style.display = 'none'", zendesk)
#     # except Exception:
#     #     pass
#
#     # make screenshots
#     test_name = request.function.__name__
#     driver._test_fn_name = test_name
#
#     yield driver
#
#     try:
#         driver.make_screenshot('final')
#     except:
#         pass
#
#     driver.quit()


@fixture(scope="session")
def drv(app_config):
    browser = app_config.browser[0]
    if (ARGS := app_config.browser[1]) is not None:
        drv = browser(options=ARGS)
    else:
        drv = browser()

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
    config_param = {
        "env": request.config.getoption("--env"),
        "browser": request.config.getoption("--browser")
    }
    return config_param


@fixture(scope="session")
def app_config(get_parameters):
    configuration = Config(get_parameters)
    return configuration
