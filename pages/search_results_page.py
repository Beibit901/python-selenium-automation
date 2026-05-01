from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")

    def verify_search_results(self, product: str):
        self.verify_partial_text(product, *self.SEARCH_RESULT_COUNT_TEXT)

    def verify_url_product(self, product):
        self.wait_until_url_contains(product)
