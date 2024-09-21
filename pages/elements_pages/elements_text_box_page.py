from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsTextBoxPage(BasePage):
    __URL = "https://demoqa.com/text-box"
    __FULL_NAME = (By.CSS_SELECTOR, "#userName")
    __EMAIL = (By.CSS_SELECTOR, "#userEmail")
    __CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[placeholder='Current Address']")
    __PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    __SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    __FILLED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    __FILLED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    __FILLED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    __FILLED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        self._open(self.__URL)

    def fill_form(self, full_name: str, email: str, current_address: str, permanent_address: str):
        self._type(self.__FULL_NAME, full_name)
        self._type(self.__EMAIL, email)
        self._type(self.__CURRENT_ADDRESS, current_address)
        self._type(self.__PERMANENT_ADDRESS, permanent_address)

    def submit_form(self):
        self._scroll_to_element(self._find(self.__SUBMIT_BUTTON))
        self._click(self.__SUBMIT_BUTTON)

    def filed_data(self):
        actual_full_name = self._get_text(self.__FILLED_FULL_NAME).split(":")[1]
        actual_email = self._get_text(self.__FILLED_EMAIL).split(":")[1]
        actual_current_address = self._get_text(self.__FILLED_CURRENT_ADDRESS).split(":")[1]
        actual_permanent_address = self._get_text(self.__FILLED_PERMANENT_ADDRESS).split(":")[1]
        return actual_full_name, actual_email, actual_current_address, actual_permanent_address
