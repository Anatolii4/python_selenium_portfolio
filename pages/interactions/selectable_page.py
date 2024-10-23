import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SelectablePage(BasePage):
    __URL = "https://demoqa.com/selectable"
    __LIST_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-list]")
    __LIST_ITEM = (By.CSS_SELECTOR, "div[id=demo-tabpane-list] li[class='mt-2 list-group-item list-group-item-action']")
    __LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "div[id=demo-tabpane-list] li[class='mt-2 list-group-item active list-group-item-action']")
    __GRID_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-grid]")
    __GRID_ITEM = (By.CSS_SELECTOR, "div[id=demo-tabpane-grid] li[class='list-group-item list-group-item-action']")
    __GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "div[id=demo-tabpane-grid] li[class='list-group-item active list-group-item-action']")

    def open_page(self):
        super()._open(self.__URL)

    def click_selectable_item(self, elements):
        item_list = super()._find_elements(elements)
        item1, item2 = random.sample(item_list, k=2)
        super()._scroll_to_element(item1)
        item1.click()
        super()._scroll_to_element(item2)
        item2.click()

    def select_list_items(self):
        self.click_selectable_item(self.__LIST_ITEM)
        active_item_list = super()._find_elements(self.__LIST_ITEM_ACTIVE)
        return len(active_item_list)

    def select_grid_items(self):
        super()._click(self.__GRID_TAB)
        self.click_selectable_item(self.__GRID_ITEM)
        active_item_grid = super()._find_elements(self.__GRID_ITEM_ACTIVE)
        return len(active_item_grid)
