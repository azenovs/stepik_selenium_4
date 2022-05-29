from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart()

     def should_be_add_to_cart(self):
         assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "add to cart button is missing"
