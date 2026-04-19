from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/ ')
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(3)

expected_result = "Sign in or create account"
actual_result = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading__ph')]").text

assert expected_result == actual_result

actual_result = driver.find_element(By.XPATH, "//*[contains(@class,'styles_ndsHeading__phw6r')]")

print("Test passed")

driver.quit()