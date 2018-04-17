from selenium.webdriver.common.by import By


class CreateEventPageLocators:
    STATUS_MESSAGE = (By.ID, 'status-message')
    CREATE_EVENT_FORM = (By.ID, 'event-form')
    TITLE_FIELD = (By.ID, 'title')
    DESCRIPTION_FIELD = (By.ID, 'description')
    SUBMIT_BUTTON = (By.ID, 'create-event')