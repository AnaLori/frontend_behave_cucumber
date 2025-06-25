from behave import given, when, then
from features.pages.search_page import SearchPage
from features.helpers.auth_helper import login
import logging
import time

@given("I am logged in on the site")
def step_logged_in(context):
    try:
        login(context)
        time.sleep(1)  # Espera para estabilização
    except Exception as e:
        logging.error(f"Falha no login: {str(e)}")
        raise

@when('I search for the product "{product}"')
def step_search_product(context, product):
    try:
        context.product_name = product
        context.search_page = SearchPage(context.driver)
        context.search_page.search(product)
        context.product_searched = product  # Guarda o produto pesquisado para verificação
    except Exception as e:
        context.driver.save_screenshot("search_error.png")
        raise Exception(f"Erro ao buscar produto '{product}': {str(e)}")

@then("search results must be shown")
def step_verify_search(context):
    assert context.search_page.has_results(), (
        f"Nenhum resultado encontrado para '{getattr(context, 'product_searched', '')}'"
    )

@then("no results message should be shown")
def step_verify_no_results(context):
    assert context.search_page.no_results_message_visible(), (
        f"Mensagem de 'sem resultados' não apareceu para '{getattr(context, 'product_searched', '')}'"
    )