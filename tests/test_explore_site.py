import allure
from playwright.sync_api import Page


@allure.feature("Site Exploration")
def test_explore_main_page(page: Page, base_url):
    """Исследование структуры главной страницы"""
    page.goto(base_url)

    # Получаем все ссылки навигации
    links = page.locator("a").all()

    print(f"\nНайдено {len(links)} ссылок:")
    for i, link in enumerate(links[:20]):  # Первые 20 ссылок
        try:
            text = link.text_content()
            href = link.get_attribute("href")
            if text and text.strip():
                print(f"{i+1}. Текст: '{text.strip()}' | href: '{href}'")
        except Exception:
            continue

    # Проверяем заголовок страницы
    title = page.title()
    print(f"\nЗаголовок страницы: {title}")

    assert title  # Просто проверяем что страница загрузилась
