from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    PAGE_BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    CART_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
