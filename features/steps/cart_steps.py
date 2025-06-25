from behave import given, when, then
from features.pages.product_page import ProductPage
from features.pages.cart_page import CartPage
from features.pages.search_page import SearchPage
from features.helpers.auth_helper import login
import time


@when('I click in the product "{product}"')
def step_click_product(context, product):
    context.product_name = product
    context.product_page = ProductPage(context.driver)
    context.product_page.click_product_by_name(context.product_name)
    time.sleep(2)  # Espera para carregar a página do produto

@when("add it to cart")
def step_add_to_cart(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.add_to_cart()

@then('the product must be in the cart')
def verify_checkout_product(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.verify_product()