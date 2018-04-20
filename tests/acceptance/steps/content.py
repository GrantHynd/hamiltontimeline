from behave import *
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.create_event_page import CreateEventPage

use_step_matcher('re')


@then('I see a status message "(.*)"')
def step_impl(context, status_message):
    page = CreateEventPage(context.driver)
    assert status_message in page.status_message.get_attribute("innerHTML")


@then('I see an event with the title "(.*)"')
def step_impl(context, title):
    page = HomePage(context.driver)
    events_with_title = [event for event in page.events if event.text == title]
    print(events_with_title)
    assert len(events_with_title) > 0
    assert all([post.is_displayed() for post in events_with_title])

