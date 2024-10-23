import random
import time
import re

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DraggablePage(BasePage):
    __URL = "https://demoqa.com/dragabble"
    __DRUG_ME_SIMPLE = (By.CSS_SELECTOR, "div[id=dragBox]")

    __AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id=draggableExample-tab-axisRestriction]")
    __ONLY_X = (By.CSS_SELECTOR, "div[id=restrictedX]")
    __ONLY_Y = (By.CSS_SELECTOR, "div[id=restrictedY]")

    def __init(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_drag_simple(self):
        drag_me = super()._find(self.__DRUG_ME_SIMPLE)
        super()._scroll_to_element(drag_me)
        initial_location = drag_me.location
        super()._drag_and_drop_by_offset(drag_me, random.randint(10,100), random.randint(10,100))
        final_location = drag_me.location
        return initial_location, final_location

    def check_x_axis_restricted(self):
        super()._click(self.__AXIS_RESTRICTED_TAB)
        only_x_element = super()._find(self.__ONLY_X)
        super()._scroll_to_element(only_x_element)
        super()._wait_until_element_is_visible(self.__ONLY_X)
        super()._drag_and_drop_by_offset(only_x_element, 100,100)
        only_x_final_location = only_x_element.get_attribute("style")
        only_x_final_location_modified = only_x_final_location.split("position: relative; left: 100px;")[1].split("px")[0].strip()
        return only_x_final_location_modified

    def check_y_axis_restricted(self):
        super()._click(self.__AXIS_RESTRICTED_TAB)
        only_x_element = super()._find(self.__ONLY_Y)
        super()._scroll_to_element(only_x_element)
        super()._wait_until_element_is_visible(self.__ONLY_Y)
        super()._drag_and_drop_by_offset(only_x_element, 100,100)
        only_y_final_location = only_x_element.get_attribute("style")
        only_y_final_location_modified = re.findall(r'\d[0-9]|\d', only_y_final_location.split(";")[1])
        return only_y_final_location_modified