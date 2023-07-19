import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(2)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(2)
    