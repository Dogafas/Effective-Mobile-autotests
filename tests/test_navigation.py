import allure
import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("Navigation Tests")
class TestNavigation:
    @pytest.mark.parametrize(
        "method_name,expected_fragment",
        [
            ("click_about_us", "#about"),
            ("click_contacts", "#contacts"),
            ("click_services", "#moreinfo"),
            ("click_cases", "#cases"),
            ("click_reviews", "#Reviews"),
            ("click_specialists", "#specialists"),
            ("click_more_info", "#moreinfo"),
        ],
    )
    @allure.story("Section Navigation")
    def test_section_navigation(
        self, page: Page, base_url, method_name, expected_fragment
    ):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Вызываем метод навигации
        getattr(main_page, method_name)()

        # Проверяем переход
        current_url = main_page.get_current_url()
        assert expected_fragment in current_url
