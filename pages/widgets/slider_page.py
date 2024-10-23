import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SliderPage(BasePage):
    __URL = "https://demoqa.com/slider"
    __SLIDER_BAR = (By.CSS_SELECTOR, "input[type='range']")
    __SLIDER_VALUE = (By.CSS_SELECTOR, "input[id=sliderValue]")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_slider(self):
        slide_value_before = super()._find(self.__SLIDER_VALUE).get_attribute("value")
        slider_input = super()._find(self.__SLIDER_BAR)
        x_coordinate = random.randint(1, 100)
        super()._drag_and_drop_by_offset(slider_input, x_coordinate, 0)
        value_after_changing = super()._find(self.__SLIDER_VALUE).get_attribute("value")
        return slide_value_before, value_after_changing