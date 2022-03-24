from pytest import mark
from time import sleep

'''
# 1 Форма - Положительная проверка - Ввести корректные данные в поле Your name
# https://docs.google.com/document/d/1rptt8V_Z5qcc3lU-_SR_zr96w9TNqmVuWa1l04jFYFA/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("name", ["Иванов Иван", "Paul Smith"])
def test_correct_name_input(form_page, app_config, name):
    form_page.go(app_config.base_url)

    form_page.name_input_field.input_text(f"{name}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(1).is_visible():
        assert False
    else:
        assert True


# 2 Форма - Положительная проверка - Ввести корректные данные в поле Email
# https://docs.google.com/document/d/1zVVk2sC05R3MCL9eGY4yeE2orVct_3zGEbmrTiNPbhY/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("email", ["test@mail.fake.eu", "anatoly.rozhkov1998@gmail.com",
                           "somefakeperson@yandex.ru", "johndoeyahoo@mail.com"])
def test_correct_email_input(form_page, email):
    form_page.email_input_field.input_text(f"{email}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(2).is_visible():
        assert False
    else:
        assert True


# 3 Форма - Положительная проверка - Выбрать страну в дропдауне с флагами
# https://docs.google.com/document/d/1Ks2-c0DFShDtS330IlY0SaZWFU1dTP-AkExsaYMEQNU/edit?usp=sharing
@mark.ui
@mark.form_page
def test_correct_country_code_selection(form_page):
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()

    if form_page.country_code.text == "+7":
        assert True
    else:
        assert False


# 4 Форма - Положительная проверка - Ввести корректные данные в поле Your phone
# https://docs.google.com/document/d/1rjbI62OkE9eXF-pere1pwMxoiF3SEY8ESr4krPLJVHo/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("phone", ["(456) 756-70-45", "(655) 764-25-34"])
def test_correct_phone_number(form_page, phone):
    form_page.phone_input_field.input_text(f"{phone}")
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(3).is_visible():
        assert False
    else:
        assert True


# 5 Форма - Положительная проверка - Отметить чекбоксы в разделе Test on devices
# https://docs.google.com/document/d/1BD5362ictySe9G1cmJlNM_-wIkDOjZXvuPioCxvAdKk/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("option", ["Samsung Galaxy s21", "PC: Windows 10"])
def test_correct_checkbox_options(form_page, option):
    form_page.select_checkbox_at_index(2).perform_click()
    form_page.select_checkbox_at_index(3).perform_click()
    form_page.send_button.perform_click()
    options = form_page.checkbox_value_holder.value

    if option in options:
        assert True
    else:
        assert False

# 6 Форма - Полжительная проверка - Выбрать вариант из дропдауна Select automation technology
# https://docs.google.com/document/d/1gaiHnJWbtE9xqMCkcav861SzEW_n0JOxoK-V57I3W_8/edit?usp=sharing
@mark.ui
@mark.form_page
def test_correct_dropdown_selection(form_page):
    form_page.select_dropdown_option_at_index(3).perform_click()

    if form_page.dropdown_value_holder.value == "JS Cypress":
        assert True
    else:
        assert False

# 7 Форма - Положительная проверка - Ввести бюджет в поле Budget in USD
# https://docs.google.com/document/d/1TDHpwD2F_YSc8giMl2cAueGxD8W1iRp9kjqWMy42x_k/edit?usp=sharing
@mark.ui
@mark.form_page
def test_correct_budget_input(form_page):
    form_page.budget_in_usd_input_field.input_text("200")

    if form_page.budget_in_usd_input_field.value == "200":
        assert True
    else:

# 8 Форма - Положительная проверка - Нажать на кнопку +
# https://docs.google.com/document/d/1eH6JU4oMPrc21p3S0ZoKFP9kMBmVyM1QiV2qskZnq-8/edit?usp=sharing
@mark.ui
@mark.form_page
def test_press_plus_button(form_page):
    form_page.plus_button.perform_click()

    if form_page.budget_in_usd_input_field.value == "101":
        assert True
    else:
        assert False


# 9 Форма - Положительная проверка - Нажать на кнопку минус
# https://docs.google.com/document/d/1c0QaE0AEmQx7v3lROKXaoYfReQtTkF0sCFTjn7cTogA/edit?usp=sharing
@mark.ui
@mark.form_page
def test_press_plus_button(form_page):
    form_page.minus_button.perform_click()

    if form_page.budget_in_usd_input_field.value == "99":
        assert True
    else:
        assert False
'''
# 10 Форма - Положительная проверка - Корректно заполнить форму и отправить ее
# https://docs.google.com/document/d/1sh8a4CL6c05pqZIbzK1JqztpSLhOy7MMnhJWhGUspZ0/edit?usp=sharing
@mark.ui
@mark.form_page
def test_submit_form(form_page, app_config):
    form_page.go(app_config.base_url)

    form_page.name_input_field.input_text("Иван Иванович")
    form_page.email_input_field.input_text("ivanivanovich@mail.com")
    form_page.phone_input_field.input_text("(456) 756-70-45")
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()
    form_page.select_checkbox_at_index(1).perform_click()
    form_page.send_button.perform_click()

    sleep(5)
    if form_page.success_message.is_visible():
        assert True
    else:
        assert False


