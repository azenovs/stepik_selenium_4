from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    LIST_OF_GOODS_HEADER = (By.CSS_SELECTOR, ".basket-title")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD_REGISTER = (By.CSS_SELECTOR, "[name=registration-email]")
    PASSWORD_FIELD_REGISTER = (By.CSS_SELECTOR, "[name=registration-password1]")
    PASSWORD_CONFIRM_FIELD_REGISTER = (By.CSS_SELECTOR, "[name=registration-password2]")
    CONF_REGISTRATION = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    PAGE_BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    CART_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
