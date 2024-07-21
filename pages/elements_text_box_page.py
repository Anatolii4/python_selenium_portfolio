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
        self.open(self.__URL)

    def fill_form(self):
        self._type(self.__FULL_NAME, "Antony")
        self._type(self.__EMAIL, "Antony@gmail.com")
        self._type(self.__CURRENT_ADDRESS, "Krakow, ul.Lwowska 1")
        self._type(self.__PERMANENT_ADDRESS, "Warszawa, Lenina 5a")

    def submit_form(self):
        self._scroll_to_element(self._find(self.__SUBMIT_BUTTON))
        self._click(self.__SUBMIT_BUTTON)

    def filed_data(self):
        actual_full_name = self._get_text(self.__FILLED_FULL_NAME)
        actual_email = self._get_text(self.__FILLED_EMAIL)
        actual_current_address = self._get_text(self.__CURRENT_ADDRESS)
        actual_permanent_address = self._get_text(self.__PERMANENT_ADDRESS)
