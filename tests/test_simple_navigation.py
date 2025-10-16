import allure
from playwright.sync_api import Page


@allure.feature("Simple Navigation Test")
def test_page_loads_successfully(page: Page, base_url):
    """Простой тест загрузки страницы"""
    page.goto(base_url)
    
    # Проверяем что страница загрузилась
    page.wait_for_load_state("networkidle")
    
    # Проверяем заголовок
    title = page.title()
    assert "Effective Mobile" in title
    
    # Проверяем что есть хотя бы одна ссылка навигации
    links = page.locator("a").count()
    assert links > 0