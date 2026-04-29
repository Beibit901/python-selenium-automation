from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(1)

@when('Click on Cart icon')
def click_on_cart_icon(context):
    cart_icon = context.driver.find_element(By.XPATH, '//a[@HREF="/cart?prehydrateClick=true"]')
    cart_icon.click()
    sleep(1)

@then('Verify "Your cart is empty" message is shown')
def verify_message(context):
    message = context.driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]')
    assert message.text == 'Your cart is empty'
    sleep(1)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(1)
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(1)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    message = context.driver.find_element(By.XPATH,"//h1[text()='Sign in or create account']")
    sleep(1)
    assert message.text == 'Sign in or create account'
    sleep(1)