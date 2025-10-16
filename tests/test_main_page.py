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

    @allure.story("Specialists Navigation")
    def test_specialists_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_specialists()

        current_url = main_page.get_current_url()
        assert "#specialists" in current_url

    @allure.story("More Info Button Navigation")
    def test_more_info_navigation(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        main_page.click_more_info()

        current_url = main_page.get_current_url()
        assert "#moreinfo" in current_url

    @allure.story("Magnit Popup Button")
    def test_magnit_popup_button_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Проверяем что кнопка существует
        buttons = page.locator(main_page.POPUP_MAGNIT_BUTTON)
        assert buttons.count() >= 1

    @allure.story("Slider Arrow Right")
    def test_slider_arrow_right_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Проверяем что правые стрелки слайдера существуют
        arrows = page.locator(main_page.SLIDER_ARROW_RIGHT)
        assert arrows.count() >= 1

    @allure.story("Slider Arrow Left")
    def test_slider_arrow_left_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Проверяем что левые стрелки слайдера существуют
        arrows = page.locator(main_page.SLIDER_ARROW_LEFT)
        assert arrows.count() >= 1

    @allure.story("Slider Navigation")
    def test_slider_right_arrow_click(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Кликаем по правой стрелке и проверяем что клик прошел
        arrow = page.locator(main_page.SLIDER_ARROW_RIGHT).first
        arrow.click()

        # Проверяем что страница осталась той же (нет ошибок)
        assert page.title()

    @allure.story("Slider Navigation")
    def test_slider_left_arrow_click(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Кликаем по левой стрелке и проверяем что клик прошел
        arrow = page.locator(main_page.SLIDER_ARROW_LEFT).first
        arrow.click()

        # Проверяем что страница осталась той же (нет ошибок)
        assert page.title()

    @allure.story("MyForm Popup Button")
    def test_myform_popup_button_exists(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Проверяем что кнопка myform попапа существует
        buttons = page.locator(main_page.POPUP_MYFORM_BUTTON)
        assert buttons.count() >= 1

    @allure.story("MyForm Popup Button Click")
    def test_myform_popup_button_click(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Кликаем по кнопке myform попапа
        button = page.locator(main_page.POPUP_MYFORM_BUTTON).first
        button.click()

        # Проверяем что клик прошел без ошибок
        assert page.title()
