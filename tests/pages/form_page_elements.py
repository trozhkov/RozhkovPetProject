from selenium.webdriver.common.by import By
from tests.base.base_element import BaseElement as BE
import tests.base.base_page
from tests.base.locator import Locator


class FormPageElements(tests.base.base_page.BasePage):
    @property
    def name_input_field(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//input[@name='Name']"))

    @property
    def email_input_field(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//input[@name='Email']"))

    @property
    def expand_country_flag_dropdown(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//div[@class='t-input-phonemask__select']"))

    # for example letters == "ru"
    def select_option_in_flag_dropdown_by_letters(self, letters):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value=f"//div[@id='t-phonemask_{letters}']"))

    @property
    def country_code(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[@class='t-input-phonemask__select-code']"))

    @property
    def phone_input_field(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//input[@type='tel']"))

    def select_checkbox_at_index(self, index):
        return BE(driver=self.driver,
                  locator=Locator(by=By.XPATH,
                                  value=f"/descendant::div[@class='t-checkbox__indicator'][{index}]"))

    @property
    def checkbox_value_holder(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//input[@class='t-checkboxes__hiddeninput js-tilda-rule']"))

    def select_dropdown_option_at_index(self, index):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value=f"//select/option[{index}]"))

    @property
    def dropdown_value_holder(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//select[@name='Select automation technology']"))

    @property
    def budget_in_usd_input_field(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//input[@name='Budget in USD']"))

    @property
    def minus_button(self):
        return BE(driver=self.driver,
                  locator=Locator(by=By.XPATH,
                                  value="//span[@class='t-inputquantity__btn t-inputquantity__btn-minus']"))

    @property
    def plus_button(self):
        return BE(driver=self.driver,
                  locator=Locator(by=By.XPATH,
                                  value="//span[@class='t-inputquantity__btn t-inputquantity__btn-plus']"))

    @property
    def send_button(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//button[@type='submit']"))

    def error_message_by_index(self, index):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value=f"/descendant::div[@class='t-input-error'][{index}]"))

    def error_message_under_send_by_index(self, index):
        return BE(driver=self.driver,
                  locator=Locator(by=By.XPATH,
                                  value=f"descendant::div[@class='t-form__errorbox-text t-text t-text_md']/p[{index}]"))

    @property
    def success_message(self):
        return BE(driver=self.driver,
                  locator=Locator(by=By.XPATH,
                                  value="//div[@class='js-successbox t-form__successbox t-text t-text_md']"))


class WikipediaPage(tests.base.base_page.BasePage):
    @property
    def english_lang_option(self):
        return BE(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".central-featured .lang1 strong"))


    @property
    def start_a_new_article_link(self):
        return BE(driver=self.driver, locator=Locator(by=By.XPATH, value="//*[text()='Start a new article']"))

    
    @property
    def help_us_with_other_tasks_link(self):
        return BE(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=".quotebox-quote a[title='Wikipedia:Task Center']"))
