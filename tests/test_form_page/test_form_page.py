from pytest import mark
from time import sleep
from tests.pages.form_page_elements import FormPageElements


# 1 Форма - Положительная проверка - Ввести корректные данные в поле Your name
# https://docs.google.com/document/d/1rptt8V_Z5qcc3lU-_SR_zr96w9TNqmVuWa1l04jFYFA/edit?usp=sharing
@mark.form_page
@mark.trial
@mark.ui
@mark.parametrize("name", ["Иванов Иван", "Paul Smith"])
def test_correct_name_input(drv, app_config, name):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)

    form_page.name_input_field.input_text(f"{name}")
    form_page.send_button.perform_click()
    form_page.take_screenshot()
    form_page.take_screenshot()

    if form_page.error_message_by_index(1).is_visible:
        assert False
    else:
        assert True


# 2 Форма - Положительная проверка - Ввести корректные данные в поле Email
# https://docs.google.com/document/d/1zVVk2sC05R3MCL9eGY4yeE2orVct_3zGEbmrTiNPbhY/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("email", ["test@mail.fake.eu", "anatoly.rozhkov1998@gmail.com",
                            "somefakeperson@yandex.ru", "johndoeyahoo@mail.com"])
def test_correct_email_input(drv, app_config, email):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)

    form_page.email_input_field.input_text(f"{email}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(2).is_visible:
        assert False
    else:
        assert True


# 3 Форма - Положительная проверка - Выбрать страну в дропдауне с флагами
# https://docs.google.com/document/d/1Ks2-c0DFShDtS330IlY0SaZWFU1dTP-AkExsaYMEQNU/edit?usp=sharing
@mark.ui
@mark.form_page
def test_correct_country_code_selection(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.take_screenshot()
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
@mark.error
@mark.parametrize("phone", ["(456) 756-70-45", "(655) 764-25-34"])
def test_correct_phone_number(drv, app_config, phone):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.phone_input_field.input_text(f"{phone}")
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(3).is_visible:
        assert False
    else:
        assert True


# 5 Форма - Положительная проверка - Отметить чекбоксы в разделе Test on devices
# https://docs.google.com/document/d/1BD5362ictySe9G1cmJlNM_-wIkDOjZXvuPioCxvAdKk/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("option", ["Samsung Galaxy s21", "PC: Windows 10"])
def test_correct_checkbox_options(drv, app_config, option):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
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
def test_correct_dropdown_selection(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.select_dropdown_option_at_index(3).perform_click()

    if form_page.dropdown_value_holder.value == "JS Cypress":
        assert True
    else:
        assert False


# 7 Форма - Положительная проверка - Ввести бюджет в поле Budget in USD
# https://docs.google.com/document/d/1TDHpwD2F_YSc8giMl2cAueGxD8W1iRp9kjqWMy42x_k/edit?usp=sharing
@mark.ui
@mark.form_page
def test_correct_budget_input(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.budget_in_usd_input_field.input_text("200")

    if form_page.budget_in_usd_input_field.value == "200":
        assert True
    else:
        assert False


# 8 Форма - Положительная проверка - Нажать на кнопку +
# https://docs.google.com/document/d/1eH6JU4oMPrc21p3S0ZoKFP9kMBmVyM1QiV2qskZnq-8/edit?usp=sharing
@mark.ui
@mark.form_page
def test_press_plus_button(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.plus_button.perform_click()

    if form_page.budget_in_usd_input_field.value == "101":
        assert True
    else:
        assert False


# 9 Форма - Положительная проверка - Нажать на кнопку минус
# https://docs.google.com/document/d/1c0QaE0AEmQx7v3lROKXaoYfReQtTkF0sCFTjn7cTogA/edit?usp=sharing
@mark.ui
@mark.form_page
def test_press_minus_button(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.minus_button.perform_click()

    if form_page.budget_in_usd_input_field.value == "99":
        assert True
    else:
        assert False


# 10 Форма - Положительная проверка - Корректно заполнить форму и отправить ее
# https://docs.google.com/document/d/1sh8a4CL6c05pqZIbzK1JqztpSLhOy7MMnhJWhGUspZ0/edit?usp=sharing
@mark.ui
@mark.error
@mark.special
def test_submit_form(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.name_input_field.input_text("Иван Иванович")
    form_page.email_input_field.input_text("ivanivanovich@mail.com")
    form_page.phone_input_field.input_text("(456) 756-70-45")
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()
    form_page.select_checkbox_at_index(1).perform_click()
    form_page.send_button.perform_click()

    # wait till the next page loads
    sleep(1)

    if form_page.success_message.is_visible:
        assert True
    else:
        assert False


# 11 Форма - Негативная проверка - Оставить поля пустыми
# https://docs.google.com/document/d/1UjSanU3taRZ9kHG4ZMlxTuu6Wuamq35ZhAgPcCYtauI/edit?usp=sharing
@mark.ui
@mark.form_page
def test_all_fields_empty(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(1).is_visible and \
            form_page.error_message_by_index(2).is_visible and \
            form_page.error_message_by_index(3).is_visible and \
            form_page.error_message_by_index(4).is_visible and \
            form_page.error_message_under_send_by_index(2):
        assert True
    else:
        assert False


# 12 Фомра - Негативная проверка - Ввести некорректное данные в поля Your name
# https://docs.google.com/document/d/1dhx9Vip1PBxO9WmCbcwtRDb82ejGQze5dfapHDZJH8c/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.error
@mark.parametrize("incorrect_name", ["Ivan Ivanov1", "Иванов Иван@#", "342@3$дфг",
                                     "                    Иванов Иван"])
def test_incorrect_name_input(drv, app_config, incorrect_name):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.name_input_field.input_text(f"{incorrect_name}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(1).is_visible:
        assert True
    else:
        assert False


# 13 Форма - Негативная проверка - Ввести некорректныe данные в поле Your Email
# https://docs.google.com/document/d/1PH4NtOJ-aBKkGbnAkQeewwEizA5eaxLRHNy2csU89gU/edit?usp=sharing
@mark.ui
@mark.error
@mark.form_page
@mark.parametrize("incorrect_email", ["asdf@", "маил@маил.сом", "mail@domain",
                                      "mail@domain", "m@ail@domain.com", "m#ail@domain.com",
                                      "m,ail@domain.com"])
def test_incorrect_email_input(drv, app_config, incorrect_email):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.email_input_field.input_text(f"{incorrect_email}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(2).is_visible:
        assert True
    else:
        assert False


# 14 Форма - Негативная проверка - Ввести некорректный данные в поле Your phone
# https://docs.google.com/document/d/1UZ8KhEHYct9ThgBjks29mfttC1-RYCOvIeLDu84myLQ/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("incorrect_phone", ["(454) 343", "(454) 343-23", "adfads",
                                      "q234SDF#@-", "000,000"])
def test_incorrect_phone_input(drv, app_config, incorrect_phone):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.phone_input_field.input_text(f"{incorrect_phone}")
    form_page.expand_country_flag_dropdown.perform_click()
    form_page.select_option_in_flag_dropdown_by_letters("ru").perform_click()
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(3).is_visible:
        assert True
    else:
        assert False


# 15 Форма - Негативная проверка - Ввести некорректные данные в поле Budget in USD
# https://docs.google.com/document/d/17E-PKFEGAASimougYDoMR2PuWovb0gC3LiSHTAJub3E/edit?usp=sharing
@mark.ui
@mark.form_page
@mark.parametrize("incorrect_budget_input", ["adgas", "-2342", "-2", "3*20", "3-23",
                                             "+3", "#@!", "e"])
def test_incorrect_budget_input(drv, app_config, incorrect_budget_input):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.budget_in_usd_input_field.input_text(f"{incorrect_budget_input}")
    form_page.send_button.perform_click()

    if form_page.error_message_by_index(6).is_visible:
        assert True
    else:
        assert False


# 16 Фомра - Негативная проверка - Уменьшить Budget in USD до отрицательных значений с помощю кнопки минус
# https://docs.google.com/document/d/1hPUGK9o0MQO8TY98g2n0RujbN_rDb1ag86xgje-iW_o/edit?usp=sharing
@mark.ui
@mark.form_page
def test_click_minus_button_until_negative_number(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)

    form_page.budget_in_usd_input_field.input_text("0")
    form_page.minus_button.perform_click()

    if form_page.budget_in_usd_input_field.value == "0":
        assert True
    else:
        assert False


# 17 Форма - Негативная проверка - Нажать на плюс и минус, при некорректных данных в поле Budget in USD
# https://docs.google.com/document/d/1PifMUZkkSEte1c1ZDPuHQ1gXHSlRUQbEKzO8lbEi3jM/edit?usp=sharing
@mark.ui
@mark.form_page
def test_click_plus_or_minus_with_incorrect_budget_input(drv, app_config):
    form_page = FormPageElements(drv)
    form_page.go(app_config.url)
    form_page.budget_in_usd_input_field.input_text("324SDF")
    form_page.minus_button.perform_click()
    first_input = form_page.budget_in_usd_input_field.value
    form_page.budget_in_usd_input_field.input_text("234SDF")
    form_page.plus_button.perform_click()
    second_input = form_page.budget_in_usd_input_field.value

    if first_input == "0" and second_input == "1":
        assert True
    else:
        assert False
