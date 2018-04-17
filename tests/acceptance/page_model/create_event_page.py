from selenium.webdriver.common.by import By
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.locators.create_event_page import CreateEventPageLocators


class CreateEventPage(BasePage):
    @property
    def url(self):
        base_url = super(CreateEventPage, self).url
        return base_url+'/administrator/events/create'

    @property
    def status_message(self):
        return self.driver.find_element(*CreateEventPageLocators.STATUS_MESSAGE)

    @property
    def form(self):
        return self.driver.find_element(*CreateEventPageLocators.CREATE_EVENT_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*CreateEventPageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
