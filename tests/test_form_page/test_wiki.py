from pytest import mark
from time import sleep
from tests.pages.form_page_elements import WikipediaPage


@mark.dev
def test_correct_name_input(drv):
    wiki_page = WikipediaPage(drv)
    wiki_page.go("https://www.wikipedia.org/")

    # choose english wiki
    wiki_page.english_lang_option.perform_click()
    sleep(1)

    # click on start a new article link
    wiki_page.start_a_new_article_link.perform_click()
    sleep(1)

    # click on help with other projects option
    wiki_page.help_us_with_other_tasks_link.perform_click()
    sleep(1)





