import allure
import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("UI Elements Tests")
class TestUIElements:
    @pytest.mark.parametrize(
        "locator_name,min_count",
        [
            ("POPUP_MAGNIT_BUTTON", 1),
            ("SLIDER_ARROW_RIGHT", 1),
            ("SLIDER_ARROW_LEFT", 1),
            ("POPUP_MYFORM_BUTTON", 1),
            ("CAROUSEL_BUTTON_RIGHT", 1),
            ("CAROUSEL_BUTTON_LEFT", 1),
        ],
    )
    @allure.story("Element Existence")
    def test_element_exists(self, page: Page, base_url, locator_name, min_count):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        locator = getattr(main_page, locator_name)
        elements = page.locator(locator)
        assert elements.count() >= min_count

    @pytest.mark.parametrize(
        "locator_name",
        [
            "SLIDER_ARROW_RIGHT",
            "SLIDER_ARROW_LEFT",
            "CAROUSEL_BUTTON_RIGHT",
            "CAROUSEL_BUTTON_LEFT",
        ],
    )
    @allure.story("Element Clickability")
    def test_element_clickable(self, page: Page, base_url, locator_name):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        locator = getattr(main_page, locator_name)
        element = page.locator(locator).first
        element.click()

        # Проверяем что страница осталась стабильной
        assert page.title()

    @pytest.mark.parametrize(
        "locator_name",
        [
            "POPUP_MYFORM_BUTTON",
        ],
    )
    @allure.story("Popup Button Click")
    def test_popup_button_click(self, page: Page, base_url, locator_name):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        locator = getattr(main_page, locator_name)
        button = page.locator(locator).first
        button.click()

        # Проверяем что клик прошел без ошибок
        assert page.title()
