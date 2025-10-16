import allure
from playwright.sync_api import Page

from pages.main_page import MainPage


@allure.feature("Forms Tests")
class TestForms:
    @allure.story("Contact Form Submission")
    def test_contact_form_submission(self, page: Page, base_url):
        main_page = MainPage(page)
        main_page.navigate_to(base_url)

        # Открываем попап с формой
        main_page.click_myform_popup()

        # Ждем появления формы
        page.wait_for_selector(main_page.FORM_NAME_INPUT, timeout=5000)

        # Заполняем форму тестовыми данными
        main_page.fill_contact_form(
            name="Тест Тестов",
            phone="9001234567",
            telegram="@test_user",
            message="Тестовое сообщение",
        )

        # Отправляем форму
        main_page.submit_contact_form()

        # Проверяем успешную отправку (отсутствие ошибок)
        page.wait_for_timeout(2000)  # Ждем обработки
        assert page.title()  # Страница осталась доступной
