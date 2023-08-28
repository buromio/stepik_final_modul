import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not contain 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on the login page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present on the login page"

    self.should_be_login_url()
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL does not contain 'login' substring"


promo_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.parametrize('link', promo_links)

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

promo_links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
               #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                            #marks=pytest.mark.xfail),
               # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
               #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
              ]

@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_basket_total_equal_to_product_price()
    page.success_message_should_disappear()  # элемент присутствует на странице и должен исчезнуть

