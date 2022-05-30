from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # checking correctness of an url
    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", \
            f"expected login page, received {self.browser.current_url}"

    # checking presence of the login form
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is missing"

    # checking presence of the register form
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is missing"

    # registering a new user
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD_REGISTER)
        email_field.send_keys(email)
        pw1_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTER)
        pw1_field.send_keys(password)
        pw2_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD_REGISTER)
        pw2_field.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.CONF_REGISTRATION)
        confirm_button.click()
