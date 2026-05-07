from selenium.webdriver.common.by import By
from behave import given, when, then

from pages.cart import Cart

CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_msg(context):
    actual = context.app.cart.empty_cart()
    expected = 'Your cart is empty'
    context.app.cart.verify_equal(actual, expected)

