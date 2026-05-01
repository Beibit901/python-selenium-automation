from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

ITEM_ID= (By.ID, 'addToCartButtonOrTextIdFor54406334')
ITEM_ADD= (By.ID, 'addToCartButtonOrTextIdFor93867402')

@when("Add Item to cart")
def add_item(context):
    context.driver.find_element(*ITEM_ID).click()
    context.driver.find_element(*ITEM_ADD).click()

@when("Close adding item")
def close_add_item(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="close"]').click()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_msg(context):
    actual = context.driver.find_element(*CART_EMPTY_MSG).text
    expected = 'Your cart is empty'
    assert actual == expected, f'Expected {expected} did not match actual {actual}'

@then("Verify Item in cart or total prices")
def verify_cart(context):
    texts = context.driver.find_element(By.XPATH, '//*[@data-test="cartItem-price"]').get_attribute("textContent").strip()
    assert "$29.49" in texts, f'Expected "$29.49" in {texts}'
