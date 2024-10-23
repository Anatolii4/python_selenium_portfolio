from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class FramePage(BasePage):
    __URL = "https://demoqa.com/frames"
    __FRAME1 = (By.CSS_SELECTOR, "iframe[id=frame1]")
    __FRAME2 = (By.CSS_SELECTOR, "iframe[id=frame2]")
    __TITLE_FRAME = (By.CSS_SELECTOR, "h1[id=sampleHeading]")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame_locator = self.__FRAME1
        elif frame_num == "frame2":
            frame_locator = self.__FRAME2
        else:
            raise ValueError("The frame is not correct")
        frame = super()._find(frame_locator)
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        super()._switch_to_frame(frame)
        text = super()._find(self.__TITLE_FRAME).text
        super()._switch_to_default_content()
        return [width, height, text]
