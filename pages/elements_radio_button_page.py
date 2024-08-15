import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsRadioButtonPage(BasePage):
    __URL = "https://demoqa.com/radio-button"
    __RADIO_BUTTONS_LOCATOR = (By.CSS_SELECTOR, "label[class='custom-control-label']")
    __OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        self._open(self.__URL)

    def click_random_radio_button(self) -> str:
        radio_buttons = self._find_elements(self.__RADIO_BUTTONS_LOCATOR)
        random_button = random.choice(radio_buttons)
        random_button.click()
        return random_button.text

    def get_output_result(self) -> str:
        result = self._find(self.__OUTPUT_RESULT).text
        return result

