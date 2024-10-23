from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class MenuPage(BasePage):
    __URL = "https://demoqa.com/menu"
    __MENU_LOCATOR = (By.CSS_SELECTOR, "ul[id=nav] li a")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open(self.__URL)

    def check_menu(self):
        menu_list = super()._wait_until_menu_are_present(self.__MENU_LOCATOR)
        data = []
        for item in menu_list:
            super()._scroll_to_element(item)
            super()._move_to_element(item)
            data.append(item.text)
        return data
