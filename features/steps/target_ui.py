from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify that it is correct Correct {paragraph}')
def verify_heading(context, paragraph):
    headings = context.driver.find_elements(By.CSS_SELECTOR, ".styles_ndsHeading__phw6r")
    texts = [heading.text.strip() for heading in headings]
    print(texts)
    assert paragraph in texts, f'Expected "{paragraph}", but found {texts}'

@then("verify 9 help categories under 'What would you like help with?'")
def verify_link_number(context):
    cards = context.driver.find_elements(By.CSS_SELECTOR, ".NavigationCard_isFullWidth__7vBve")
    assert len(cards) == 9, f"Expected 9, got {len(cards)}"


@then("verify 8 categories under 'Popular Pages'")
def verify_link_number(context):
    cards = context.driver.find_elements(By.CSS_SELECTOR, ".LinkItem_linkList__HYpuy")
    assert len(cards) == 8, f"Expected 8, got {len(cards)}"


@then("verify Search bar")
def verify_link_number(context):
    search_bar = context.driver.find_element(By.CSS_SELECTOR, ".HelpSearch_typeAheadContainer__JS29u")
    assert search_bar.is_displayed()


@then("verify Search button")
def verify_link_number(context):
    search_button = context.driver.find_element(By.CSS_SELECTOR, ".styles_bare__kmwJn")
    assert search_button.is_displayed()

@then("verify 'Browse all help' button")
def verify_link_number(context):
    text = context.driver.find_element(By.XPATH, "//*[contains(@class, 'FlyoutKnowledge_styledButton__Uoded')]").text
    assert text == "Browse all help", f"Expected 'Browse all help', got {text}"
