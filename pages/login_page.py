from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_CONFIRM_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BTN).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not current"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"
