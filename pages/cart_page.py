from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    # copy
    cart_empty_copy = 'Your cart is empty'

    def verify_cart_empty_msg(self):
        self.wait_until_appear(*self.CART_EMPTY_MSG)
        self.verify_text(self.cart_empty_copy, *self.CART_EMPTY_MSG)
