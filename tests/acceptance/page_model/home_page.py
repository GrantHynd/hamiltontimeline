from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        base_url = super(HomePage, self).url
        return base_url+'/'

    @property
    def timeline(self):
        return self.driver.find_element(*HomePageLocators.TIMELINE)

    @property
    def events(self):
        return self.driver.find_elements(*HomePageLocators.EVENT_TITLE)