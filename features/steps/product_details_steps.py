from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/women-s-cloud-knit-long-sleeve-notch-collar-top-and-pants-pajama-set-auden/-/A-94889234?preselect=94879834#lnk=sametab')
    context.wait.until(
        ec.presence_of_all_elements_located(COLOR_OPTIONS)
    )


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Light Pink', 'Light Blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(2)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'