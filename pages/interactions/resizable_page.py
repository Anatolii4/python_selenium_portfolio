import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResizablePage(BasePage):
    __URL = "https://demoqa.com/resizable"
    __RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, "div[id=resizableBoxWithRestriction] span["
                                               "class='react-resizable-handle react-resizable-handle-se']")
    __RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id=resizableBoxWithRestriction]")
    __RESIZABLE_HANDLE = (By.CSS_SELECTOR, "div[id=resizable] span[class='react-resizable-handle react-resizable-handle-se']")
    __RESIZABLE  = (By.CSS_SELECTOR, "div[id=resizable]")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def get_px_from_width_height(self, size):
        width = size.split("width:")[1].split("px")[0].strip()
        height = size.split("height:")[1].split("px")[0].strip()
        return width, height

    def get_current_size(self, element):
        element_locator = super()._find(element)
        size_value = element_locator.get_attribute("style")
        return size_value

    def change_resizable_box(self):
        resizable_box = super()._find(self.__RESIZABLE_BOX_HANDLE)
        super()._scroll_to_element(resizable_box)
        super()._drag_and_drop_by_offset(resizable_box, 100, 250)
        box_changed_size = self.get_px_from_width_height(self.get_current_size(self.__RESIZABLE_BOX))
        return box_changed_size

    def change_resizable(self):
        resizable = super()._find(self.__RESIZABLE_HANDLE)
        super()._scroll_to_element(resizable)
        super()._drag_and_drop_by_offset(resizable, -100, -150)
        changed_resizable = self.get_px_from_width_height(self.get_current_size(self.__RESIZABLE))
        return changed_resizable

