from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.create_event_page import CreateEventPageLocators

use_step_matcher('re')


@given('I wait for the status message to appear')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        expected_conditions.visibility_of_element_located(CreateEventPageLocators.STATUS_MESSAGE)
    )
