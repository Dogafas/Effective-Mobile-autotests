from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы для основных разделов
    ABOUT_US_LINK = "text=О нас"
    CONTACTS_LINK = "text=Контакты"
    SERVICES_LINK = "text=Услуги"
    CASES_LINK = "text=Кейсы"
    REVIEWS_LINK = "text=Отзывы"

    def click_about_us(self):
        self.click_element(self.ABOUT_US_LINK)

    def click_contacts(self):
        self.click_element(self.CONTACTS_LINK)

    def click_services(self):
        self.click_element(self.SERVICES_LINK)

    def click_cases(self):
        self.click_element(self.CASES_LINK)

    def click_reviews(self):
        self.click_element(self.REVIEWS_LINK)
