import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    __URL = "https://demoqa.com/auto-complete"
    __MULTI_INPUT = (By.CSS_SELECTOR, "input[id=autoCompleteMultipleInput]")
    __MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    __REMOVE_MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_auto_complete(self):
        list_of_colors = ["Red", "Blue", "Yellow", "Green", "Purple", "Black", "Voilet", "White", "Indigo", "Magenta", "Aqua"]
        number_of_colors = random.randint(2, len(list_of_colors))
        selected_colors = random.sample(list_of_colors, number_of_colors)
        for color in selected_colors:
            input_locator = super()._find(self.__MULTI_INPUT)
            super()._scroll_to_element(input_locator)
            input_locator.send_keys(color)
            input_locator.send_keys(Keys.ENTER)
        inputted_value = super()._find_elements(self.__MULTI_VALUE)
        saved_colors = []
        for i in inputted_value:
            saved_colors.append(i.text)
        return selected_colors, saved_colors

    def remove_value(self):
        count_value_before = len(super()._find_elements(self.__MULTI_VALUE))
        remove_button_list = super()._find_elements(self.__REMOVE_MULTI_VALUE)
        for i in remove_button_list:
            i.click()
            break
        count_value_after = len(super()._find_elements(self.__MULTI_VALUE))
        return count_value_before, count_value_after
