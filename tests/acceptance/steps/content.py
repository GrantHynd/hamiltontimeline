from behave import *
from tests.acceptance.page_model.create_event_page import CreateEventPage

use_step_matcher('re')


@then('I see a status message "(.*)"')
def step_impl(context, status_message):
    page = CreateEventPage(context.driver)
    assert status_message in page.status_message.get_attribute("innerHTML")
