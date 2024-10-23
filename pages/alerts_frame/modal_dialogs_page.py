from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    __URL = "https://demoqa.com/modal-dialogs"
    __SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id=showSmallModal]")
    __LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id=showLargeModal]")
    __CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id=closeSmallModal]")
    __CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[class='close']")
    __LARGE_MODAL_TEXT = (By.CSS_SELECTOR, "p")
    __SMALL_MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_small_modal(self):
        super()._click(self.__SMALL_MODAL_BUTTON)
        modal_text = super()._get_text(self.__SMALL_MODAL_TEXT)
        super()._click(self.__CLOSE_SMALL_MODAL_BUTTON)
        return modal_text

    def check_large_modal(self):
        element_locator = super()._find(self.__LARGE_MODAL_BUTTON)
        super()._scroll_to_element(element_locator)
        super()._click(self.__LARGE_MODAL_BUTTON)
        modal_text = super()._get_text(self.__LARGE_MODAL_TEXT)
        super()._click(self.__CLOSE_LARGE_MODAL_BUTTON)
        return modal_text