from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы для основных разделов
    ABOUT_US_LINK = "a.tn-atom[href='#about']"
    CONTACTS_LINK = "a.tn-atom[href='#contacts']"
    SERVICES_LINK = "a.tn-atom[href='#moreinfo']"
    CASES_LINK = "a.tn-atom[href='#cases']"
    REVIEWS_LINK = "a.tn-atom[href='#Reviews']"
    SPECIALISTS_LINK = "a.tn-atom[href='#specialists']"
    MORE_INFO_LINK = "a.tn-atom[href='#moreinfo']:has-text('Подробнее')"
    POPUP_MAGNIT_BUTTON = "a[href='#popup:magnit'] td[data-field='li_buttontitle']"
    SLIDER_ARROW_RIGHT = ".t-slds__arrow_body-right"
    SLIDER_ARROW_LEFT = ".t-slds__arrow_body-left"

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

    def click_specialists(self):
        self.click_element(self.SPECIALISTS_LINK)

    def click_more_info(self):
        self.click_element(self.MORE_INFO_LINK)

    def click_magnit_popup(self):
        self.click_element(self.POPUP_MAGNIT_BUTTON)

    def click_slider_arrow_right(self):
        self.click_element(self.SLIDER_ARROW_RIGHT)

    def click_slider_arrow_left(self):
        self.click_element(self.SLIDER_ARROW_LEFT)
