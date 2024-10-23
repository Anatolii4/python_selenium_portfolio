import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SortablePage(BasePage):
    __URL = "https://demoqa.com/sortable"
    __LIST_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-list]")
    __LIST_ITEM = (By.CSS_SELECTOR, "div[id=demo-tabpane-list] div[class='list-group-item list-group-item-action']")
    __GRID_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-grid]")
    __GRID_ITEM = (By.CSS_SELECTOR, "div[id=demo-tabpane-grid] div[class='list-group-item list-group-item-action']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def get_sorted_items(self, elements):
        items_list = super()._find_elements(elements)
        return [item.text for item in items_list]

    def change_sort_of_list(self):
        order_before = self.get_sorted_items(self.__LIST_ITEM)
        item_list = random.sample(super()._find_elements(self.__LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        super()._scroll_to_element(item_what)
        super()._scroll_to_element(item_where)
        super().drag_drop_to_element(item_what, item_where)
        order_after = self.get_sorted_items(self.__LIST_ITEM)
        return order_before, order_after

    def change_sort_of_grid(self):
        super()._click(self.__GRID_TAB)
        order_before = self.get_sorted_items(self.__GRID_ITEM)
        item_list = random.sample(super()._find_elements(self.__GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        super()._scroll_to_element(item_what)
        super()._scroll_to_element(item_where)
        super().drag_drop_to_element(item_what, item_where)
        order_after = self.get_sorted_items(self.__GRID_ITEM)
        return order_before, order_after