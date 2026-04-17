from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when("Search for tea")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)


@when("Search for coffee")
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)


@then("Verify search results for tea shown")
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'


@then("Verify search results for coffee shown")
def verify_search_results(context):
    expected_result = 'coffee'
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
    assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

