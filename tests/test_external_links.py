import allure
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("External Links Tests")
class TestExternalLinks:
    @allure.story("Telegram Link")
    def test_telegram_link_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        link = page.locator(main_page.TELEGRAM_LINK)
        assert link.count() >= 1
        assert link.first.get_attribute("target") == "_blank"
        assert link.first.get_attribute("href") == "https://t.me/assistant_em"

    @allure.story("All Telegram Links")
    def test_all_telegram_links_exist(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        links = page.locator(main_page.TELEGRAM_LINKS_ALL)
        assert links.count() >= 1

        for i in range(links.count()):
            link = links.nth(i)
            assert link.get_attribute("target") == "_blank"
            href = link.get_attribute("href")
            assert href is not None and "https://t.me/" in href

    @allure.story("Email Link")
    def test_email_link_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        link = page.locator(main_page.EMAIL_LINK)
        assert link.count() >= 1
        assert link.first.get_attribute("target") == "_blank"
        assert (
            link.first.get_attribute("href")
            == "mailto:dariia.krasnikova@effectivemobile.ru"
        )
