import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from data.data_generator.general_generator import choose_random_num_checkboxes


class ElementsCheckBoxPage(BasePage):
    __URL = "https://demoqa.com/checkbox"
    __EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
    __COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Collapse all']")
    __ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    __CHECKED_BOXES_LOCATOR = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    __CHECKED_BOX_TITLE_LOCATOR = ".//ancestor::span[@class='rct-text']"
    __LIST_OUTPUT_CHECKBOXES = (By.CSS_SELECTOR, "span[class='text-success']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        self._open(self.__URL)

    def expand_full_list(self):
        self._find(self.__EXPAND_ALL_BUTTON).click()

    def click_random_num_checkboxes(self):
        item_list = self._find_elements(self.__ITEM_LIST)
        items_to_click = random.sample(item_list, choose_random_num_checkboxes())
        for item in items_to_click:
            self._scroll_to_element(item)
            item.click()

    def get_titles_of_checked_boxes(self):
        checked_boxes = self._find_elements(self.__CHECKED_BOXES_LOCATOR)
        checked_box_titles = []
        for checkbox in checked_boxes:
            title_element = checkbox.find_element(By.XPATH, self.__CHECKED_BOX_TITLE_LOCATOR)
            checked_box_titles.append(title_element.text)
        return str(checked_box_titles).replace(" ", "").replace("doc", "").replace(".", "").lower()

    def get_output_result(self):
        result_list = self._find_elements(self.__LIST_OUTPUT_CHECKBOXES)
        output_list = []
        for result in result_list:
            output_list.append(result.text)
            output_list = [item.lower() for item in output_list]
        return str(output_list).replace(" ", "")
