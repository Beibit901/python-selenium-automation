from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@given("open the Target Circle page")
def open_target_main(context):
    context.driver.get("https://www.target.com/circle")
    sleep(2)

@given("Target Help page")
def open_target_help(context):
    context.driver.get("https://help.target.com/help")
    sleep(2)
