from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Cart(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def empty_cart(self):
        return self.find_element(*self.CART_EMPTY_MSG).text