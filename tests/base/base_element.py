from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class BaseElement(object):
    def __init__(self, driver, locator, wait_time=5):
        self.driver = driver
        self.locator = locator
        self.wait_time = wait_time

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def perform_click(self):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.click()
        return None

    def perform_click_by_enter(self):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.send_keys(Keys.RETURN)
        return None

    def input_text(self, text):
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator)
        )
        element.clear()
        element.send_keys(text)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def value(self):
        value = self.web_element.get_attribute('value')
        return value

    @property
    def class_name(self):
        value = self.web_element.get_attribute('class')
        return value

    def attribute_by_name(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def is_visible(self):
        try:
            WebDriverWait(self.driver, 0).until(
                ec.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False
