from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_text(self):
        empty_text = self.browser.find_elements(*BasketPageLocators.EMPTY_TEXT)
        assert len(empty_text) == 1, f"your basket is empty text is missing"

    def should_be_empty_goods_list(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_GOODS_HEADER), "list of goods is not empty"
