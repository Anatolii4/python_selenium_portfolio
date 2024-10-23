
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    __URL = "https://demoqa.com/progress-bar"
    __START_STOP_BUTTON = (By.CSS_SELECTOR, "button[id=startStopButton]")
    __PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[role='progressbar']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_progress_bar(self):
        button_locator = super()._find(self.__START_STOP_BUTTON)
        super()._scroll_to_element(button_locator)
        button_locator.click()
        wait_time = random.randint(1, 10)
        WebDriverWait(self.driver, 10).until(
            lambda driver: int(self._find(self.__PROGRESS_BAR_VALUE).get_attribute("aria-valuenow")) > wait_time
        )
        super()._click(self.__START_STOP_BUTTON)
        progress_bar_value_after = super()._find(self.__PROGRESS_BAR_VALUE).get_attribute("aria-valuenow")
        return progress_bar_value_after