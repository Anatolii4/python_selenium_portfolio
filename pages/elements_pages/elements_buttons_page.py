import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsButtonsPage(BasePage):

    __URL = "https://demoqa.com/buttons"
    __DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    __RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    __CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    __DOUBLE_CLICK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    __RIGHT_CLICK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    __CLICK_ME_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def click_on_different_way(self, type_click: str):
        if type_click == "double":
            element = super()._find(self.__DOUBLE_CLICK_BUTTON)
            super()._double_click(element)

        elif type_click == "right":
            element = super()._find(self.__RIGHT_CLICK_BUTTON)
            super()._right_click(element)
        elif type_click == "click":
            element = super()._find(self.__CLICK_ME_BUTTON)
            super()._scroll_to_element(element)
            super()._click(self.__CLICK_ME_BUTTON)

