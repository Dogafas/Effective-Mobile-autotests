import allure
from playwright.sync_api import Page


@allure.feature("Site Exploration")
def test_explore_main_page(page: Page, base_url):
    """Исследование структуры главной страницы"""
    page.goto(base_url)
    page.wait_for_load_state("networkidle")

    # Получаем все ссылки навигации
    links = page.locator("a").all()

    print(f"\nНайдено {len(links)} ссылок:")
    for i, link in enumerate(links[:20]):
        try:
            text = link.text_content()
            href = link.get_attribute("href")
            if text and text.strip():
                print(f"{i+1}. Текст: '{text.strip()}' | href: '{href}'")
        except Exception:
            continue

    # Ищем навигационные элементы
    print("\n=== АНАЛИЗ НАВИГАЦИИ ===")

    nav_selectors = [
        "nav a",
        "header a",
        ".menu a",
        ".navigation a",
        "[role='navigation'] a",
    ]

    for selector in nav_selectors:
        nav_links = page.locator(selector).all()
        if nav_links:
            print(f"\nНавигация ({selector}): {len(nav_links)} элементов")
            for i, link in enumerate(nav_links[:10]):
                try:
                    text = link.text_content()
                    href = link.get_attribute("href")
                    if text and text.strip():
                        print(f"  {i+1}. '{text.strip()}' -> '{href}'")
                except Exception:
                    continue

    # Проверяем заголовок страницы
    title = page.title()
    print(f"\nЗаголовок страницы: {title}")

    assert title
