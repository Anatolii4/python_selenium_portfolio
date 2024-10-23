import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    __URL = "https://demoqa.com/tool-tips"
    __HOVER_ME_BUTTON = (By.CSS_SELECTOR, "button[id=toolTipButton]")
    __BUTTON_TOOL_TIP = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
    __HOVER_INPUT_FIELD = (By.CSS_SELECTOR, "input[id=toolTipTextField]")
    __INPUT_FIELD_TOOL_TIP = (By.CSS_SELECTOR, "button[aria-describedby='textFieldToolTip']")
    __HOVER_LINK = (By.CSS_SELECTOR, "div[id=texToolTopContainer] > a:first-of-type")
    __HOVER_LINK_TIP = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
    __TOOL_TIPS_TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_tool_tips(self):
        button_tool_tip = super()._hover_and_get_text(self.__HOVER_ME_BUTTON, self.__BUTTON_TOOL_TIP, self.__TOOL_TIPS_TEXT)
        return button_tool_tip
