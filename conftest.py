from pytest import fixture
from selenium import webdriver
from tests.form_page.form_page_elements import FormPageElements
from config import Config

"""
ADD PAGE OBJECT FIXTURES
"""


@fixture(scope="session")
def form_page():
    login_page = FormPageElements(
        webdriver.Chrome()
    )
    yield login_page
    # tearing down
    print(" I am tearing down this browser")


"""
ADD PARAMETERS
"""


def pytest_addoption(parser):
    """avoid adding on letter options like -g"""
    parser.addoption("--env",
                     action="store",
                     default="dev",
                     help="Environment to run your tests against")


@fixture(scope="session")
def env(request):
    """retrieve option from the pytest_option"""
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    cfg = Config(env)
    return cfg
