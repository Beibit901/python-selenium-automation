from selenium.webdriver.common.by import By
from behave import given, when, then

@then ("verify there are {expected_amount} story cards")
def open_target_main(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, 'div.styles_row__QFU7M [data-test="@web/SlingshotComponents/common/Storycard"]')
    assert expected_amount == len(links), f'Expected {expected_amount} links but got {len(links)}'



