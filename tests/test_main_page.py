import allure
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("Main Page Navigation")
class TestMainPageNavigation:
    @allure.story("About Us Navigation")
    def test_about_us_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_about_us()

        current_url = main_page.get_current_url()
        assert "#about" in current_url

    @allure.story("Contacts Navigation")
    def test_contacts_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_contacts()

        current_url = main_page.get_current_url()
        assert "#contacts" in current_url

    @allure.story("Services Navigation")
    def test_services_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_services()

        current_url = main_page.get_current_url()
        assert "#moreinfo" in current_url

    @allure.story("Cases Navigation")
    def test_cases_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_cases()

        current_url = main_page.get_current_url()
        assert "#cases" in current_url

    @allure.story("Reviews Navigation")
    def test_reviews_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_reviews()

        current_url = main_page.get_current_url()
        assert "#Reviews" in current_url