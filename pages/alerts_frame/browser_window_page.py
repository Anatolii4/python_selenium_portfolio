from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AlertsFramePage(BasePage):
    __URL = "https://demoqa.com/browser-windows"
    __NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id=tabButton]")
    __NEW_TAB_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")
    __NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id=tabButton]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_opened_new_tab(self):
        super()._click(self.__NEW_TAB_BUTTON)
        super()._switch_to_new_tab()
        return super()._get_current_url()

    def get_new_tab_text(self):
        return super()._get_text(self.__NEW_TAB_TEXT)

    def check_opened_new_window(self):
        super()._click(self.__NEW_WINDOW_BUTTON)
        super()._switch_to_new_tab()
        return super()._get_current_url()
