import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsLinksPage(BasePage):

    __URL = "https://demoqa.com/links"
    __WORK_LINK = (By.CSS_SELECTOR, "#simpleLink")
    __BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")
    __BAD_REQUEST_HREF = "https://demoqa.com/bad-request"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_new_tab_is_open(self) -> str:
        super()._click(self.__WORK_LINK)
        super()._switch_to_new_tab()
        return super()._get_current_url()

    def check_api_request_link(self) -> int:
        bad_request_link = super()._find(self.__BAD_REQUEST)
        response = requests.get(self.__BAD_REQUEST_HREF)
        return response.status_code
