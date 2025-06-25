from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.home_page import HomePage

@given("that I am on the website's home page")
def step_open_home_page(context):
    context.login_page = LoginPage(context.driver).open()

@when('I fill in the email "{email}" and password "{password}"')
def step_fill_login_form(context, email, password):
    context.login_page.enter_email(email).enter_password(password)

@when("click on the submit button")
def step_click_login(context):
    context.login_page.submit()

@then("Validate the title after login")
def step_validate_title(context):
    assert context.login_page.is_my_account_title_visible(), "My Account title not visible after login"

@then("Validate the search products field after login")
def step_validate_search_visible(context):
    home_page = HomePage(context.driver)
    assert home_page.search_input_is_visible(), "Search field not visible after login"

