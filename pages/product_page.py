from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart()

    # checking possibility of adding an item to the basket
    def should_be_add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    # checking correctness of the book name is basket
    def should_be_correct_book_name_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.CART_BOOK_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME).text, f" \
            cart name {self.browser.find_element(*ProductPageLocators.CART_BOOK_NAME).text}, \
            page name {self.browser.find_element(*ProductPageLocators.PAGE_BOOK_NAME).text}"

    # checking correctness of the book price is basket
    def should_be_correct_book_price_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.CART_BOOK_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PAGE_BOOK_PRICE).text, f" \
            cart price {self.browser.find_element(*ProductPageLocators.CART_BOOK_PRICE).text}, \
            book price {self.browser.find_element(*ProductPageLocators.PAGE_BOOK_PRICE).text}"

    # confirming absence of success message
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    # confirming that success message disappears
    def should_disappear_success(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message didn't disappear"
