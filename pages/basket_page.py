from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # checking that "basket is empty" text is present
    def should_be_empty_text(self):
        empty_text = self.browser.find_elements(*BasketPageLocators.EMPTY_TEXT)
        assert len(empty_text) == 1, f"your basket is empty text is missing"

    # checking that there are no goods in an empty basket
    def should_be_empty_goods_list(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_GOODS_HEADER), "list of goods is not empty"
