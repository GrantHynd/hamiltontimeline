from selenium.webdriver.common.by import By


class HomePageLocators:
    TIMELINE = (By.ID, 'timeline')
    EVENT_TITLE = (By.CLASS_NAME, 'timeline__event__title')