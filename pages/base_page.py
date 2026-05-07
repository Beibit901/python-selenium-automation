class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, end_url=''):
        self.driver.get(f'https://www.target.com/{end_url}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_equal(self, actual, expected):
        assert actual == expected, f'Expected "{expected}", but got "{actual}"'