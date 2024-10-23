from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SelectMenuPage(BasePage):
    URL = "https://demoqa.com/select-menu"
    # SELECT_VALUE = (By.CSS_SELECTOR, "")
    # SELECT_ONE =
    # OLD_STYLE_MENU =
    # MULTI_SELECT_DROP_DOWN =
    # STANDART_MULTI_SELECT =

    def __init(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.URL)