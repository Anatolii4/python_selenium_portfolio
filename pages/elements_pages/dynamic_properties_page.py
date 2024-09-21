import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    __URL = "https://demoqa.com/dynamic-properties"
    __COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    __INVISIBLE_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_color_change_button(self):
        color_button = super()._find(self.__COLOR_CHANGE_BUTTON)
        color_button_initial = color_button.value_of_css_property('color')
        try:
            WebDriverWait(self.driver, 6).until(
                lambda driver: color_button.value_of_css_property('color') != color_button_initial
            )
        except TimeoutException:
            raise AssertionError("The color has not been changed within 6 seconds")
        new_color = color_button.value_of_css_property('color')
        return new_color

    def check_invisible_button(self):
        try:
            invisible_button = super()._wait_until_element_is_visible(self.__INVISIBLE_BUTTON, 6)
        except TimeoutException:
            raise AssertionError("The element is not visible after 5 seconds")