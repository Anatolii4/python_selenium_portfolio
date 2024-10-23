import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AccordianPage(BasePage):
    __URL = "https://demoqa.com/accordian"
    __SECTION1_TITLE = (By.CSS_SELECTOR, "div[id=section1Heading]")
    __SECTION1_CONTENT = (By.CSS_SELECTOR, "div[id=section1Content] >p")
    __SECTION2_TITLE = (By.CSS_SELECTOR, "div[id=section2Heading]")
    __SECTION2_CONTENT = (By.CSS_SELECTOR, "div[id=section2Content] >p")
    __SECTION3_TITLE = (By.CSS_SELECTOR, "div[id=section3Heading]")
    __SECTION3_CONTENT = (By.CSS_SELECTOR, "div[id=section3Content] >p")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_accordions(self, accordion_num):
        accordion = {
            "first": {"title": self.__SECTION1_TITLE, "content": self.__SECTION1_CONTENT},
            "second": {"title": self.__SECTION2_TITLE, "content": self.__SECTION2_CONTENT},
            "third": {"title": self.__SECTION3_TITLE, "content": self.__SECTION3_CONTENT}
        }
        title_locator = super()._find(accordion[accordion_num]["title"])
        super()._scroll_to_element(title_locator)
        if accordion_num != "first":
            super()._click(accordion[accordion_num]["title"])
        section_title = super()._get_text(accordion[accordion_num]["title"])
        section_content = super()._get_text(accordion[accordion_num]["content"])
        return section_title, section_content
