from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AlertsPage(BasePage):
    __URL = "https://demoqa.com/alerts"
    __SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id=alertButton]")
    __APPEAR_FIVE_SECOND_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id=timerAlertButton]")
    __CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id=confirmButton]")
    __PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, "button[id=promtButton]")
    __CONFIRM_BOX_RESULT = (By.CSS_SELECTOR, "span[id=confirmResult]")
    __PROMPT_BOX_RESULT = (By.CSS_SELECTOR, "span[id=promptResult]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_see_alert(self) -> str:
        super()._click(self.__SEE_ALERT_BUTTON)
        return super()._switch_to_allert()

    def check_five_sec_alert(self):
        super()._click(self.__APPEAR_FIVE_SECOND_ALERT_BUTTON)
        return super()._switch_to_allert()

    def check_confirm_box(self):
        button_locator = super()._find(self.__CONFIRM_ALERT_BUTTON)
        super()._scroll_to_element(button_locator)
        super()._click(self.__CONFIRM_ALERT_BUTTON)
        opened_alert = super()._confirm_alert()
        return opened_alert

    def get_confirm_box_result(self):
        return super()._get_text(self.__CONFIRM_BOX_RESULT)

    def check_prompt_box(self, text: str):
        button_locator = super()._find(self.__PROMPT_BOX_BUTTON)
        super()._scroll_to_element(button_locator)
        super()._click(self.__PROMPT_BOX_BUTTON)
        opened_alert = super()._prompt_alert(text)
        return opened_alert

    def get_prompt_result(self):
        return super()._get_text(self.__PROMPT_BOX_RESULT)
