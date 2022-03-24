from selenium.webdriver.common.by import By
import tests.base.base_element
import tests.base.base_page
import tests.base.locator


class FormPageElements(tests.base.base_page.BasePage):
    @property
    def name_input_field(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//input[@name='Name']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def email_input_field(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//input[@name='Email']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def expand_country_flag_dropdown(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//div[@class='t-input-phonemask__select']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    # for example letters == "ru"
    def select_option_in_flag_dropdown_by_letters(self, letters):
        locator = tests.base.locator.Locator(by=By.XPATH, value=f"//div[@id='t-phonemask_{letters}']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def country_code(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//span[@class='t-input-phonemask__select-code']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def phone_input_field(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//input[@autocomplete='tel']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    def select_checkbox_at_index(self, index):
        locator = tests.base.locator.Locator(by=By.XPATH,
                                             value=f"/descendant::div[@class='t-checkbox__indicator'][{index}]")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def checkbox_value_holder(self):
        locator = tests.base.locator.Locator(by=By.XPATH,
                                             value="//input[@class='t-checkboxes__hiddeninput js-tilda-rule']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    def select_dropdown_option_at_index(self, index):
        locator = tests.base.locator.Locator(by=By.XPATH, value=f"//select/option[{index}]")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def dropdown_value_holder(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//select[@name='Select automation technology']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def budget_in_usd_input_field(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//input[@name='Budget in USD']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def minus_button(self):
        locator = tests.base.locator.Locator(by=By.XPATH,
                                             value="//span[@class='t-inputquantity__btn t-inputquantity__btn-minus']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def plus_button(self):
        locator = tests.base.locator.Locator(by=By.XPATH,
                                             value="//span[@class='t-inputquantity__btn t-inputquantity__btn-plus']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def send_button(self):
        locator = tests.base.locator.Locator(by=By.XPATH, value="//button[@type='submit']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    def error_message_by_index(self, index):
        locator = tests.base.locator.Locator(by=By.XPATH, value=f"/descendant::div[@class='t-input-error'][{index}]")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    def error_message_under_send_by_index(self, index):
        locator = tests.base.locator.Locator(
            by=By.XPATH,
            value=f"descendant::div[@class='t-form__errorbox-text t-text t-text_md']/p[{index}]")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)

    @property
    def success_message(self):
        locator = tests.base.locator.Locator(by=By.XPATH,
                                             value="//div[@class='js-successbox t-form__successbox t-text t-text_md']")
        return tests.base.base_element.BaseElement(driver=self.driver, locator=locator)
