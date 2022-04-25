from pytest import fixture
from config import Config
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

"""
FIXTURES
"""


@fixture(scope="session")
def drv(app_config):
    yield webdriver.Chrome()


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
