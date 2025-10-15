from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click_element(self, locator: str):
        self.page.click(locator)

    def get_current_url(self) -> str:
        return self.page.url
