from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as ec

@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    context.wait.until(
        ec.element_to_be_clickable((By.XPATH, "//a[@data-test='@web/AccountLink']"))
    )


@given("open the Target Circle page")
def open_target_main(context):
    context.driver.get("https://www.target.com/circle")
    context.wait.until(
        ec.visibility_of_element_located((By.TAG_NAME, "body"))
    )

@given("Target Help page")
def open_target_help(context):
    context.driver.get("https://help.target.com/help")
    context.wait.until(
        ec.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Help')]"))
    )
