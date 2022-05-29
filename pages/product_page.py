from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart()

    def should_be_add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def should_be_correct_book_name_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.CART_BOOK_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME).text, f" \
            cart name {self.browser.find_element(*ProductPageLocators.CART_BOOK_NAME).text}, \
            page name {self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME).text}"

    def should_be_correct_book_price_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.CART_BOOK_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PAGE_BOOK_PRICE).text, f" \
            cart price {self.browser.find_element(*ProductPageLocators.CART_BOOK_PRICE).text}, \
            book price {self.browser.find_element(*ProductPageLocators.PAGE_BOOK_PRICE).text}"
