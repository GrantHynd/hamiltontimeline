from behave import *
from tests.acceptance.page_model.create_event_page import CreateEventPage

use_step_matcher('re')


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = CreateEventPage(context.driver)
    page.form_field(field_name).send_keys(content)


@when('I press the submit button')
def step_impl(context):
    page = CreateEventPage(context.driver)
    page.submit_button.click()
