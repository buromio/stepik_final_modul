from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "URL does not contain 'login' substring"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not present on the login page"

        