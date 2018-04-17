from behave import *
from selenium import webdriver
from tests.acceptance.page_model.create_event_page import CreateEventPage


@given('I am on the create event page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = CreateEventPage(context.driver)
    context.driver.get(page.url)


@then('I am on the create event page')
def step_impl(context):
    expected_url = CreateEventPage(context.driver).url
    assert context.driver.current_url == expected_url
