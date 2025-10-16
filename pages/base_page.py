from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def click_element(self, locator: str):
        self.page.click(locator, timeout=10000)

    def get_current_url(self) -> str:
        return self.page.url
