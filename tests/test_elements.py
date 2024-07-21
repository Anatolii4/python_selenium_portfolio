import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.elements_text_box_page import ElementsTextBoxPage


class TestTextBox:
    def test_submit_form(self, driver):
        text_box = ElementsTextBoxPage(driver)
        text_box.open_page()
        text_box.fill_form()
        text_box.submit_form()