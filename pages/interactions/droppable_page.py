import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DroppablePage(BasePage):
    __URL = "https://demoqa.com/droppable"
    __DRUG_ME_SIMPLE = (By.CSS_SELECTOR, "div[id=simpleDropContainer] div[id=draggable]")
    __DROP_HERE_FIELD = (By.CSS_SELECTOR, "div[id=simpleDropContainer] div[id=droppable]")

    __ACCEPT_TAB = (By.CSS_SELECTOR, "a[id=droppableExample-tab-accept]")
    __ACCEPTABLE_DRAG = (By.CSS_SELECTOR, "div[id=acceptable]")
    __NOT_ACCEPTABLE_DRAG = (By.CSS_SELECTOR, "div[id=notAcceptable]")
    __DROP_HERE_ACCEPTABLE = (By.CSS_SELECTOR, "div[id=acceptDropContainer] div[id=droppable]")

    ___PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id=droppableExample-tab-preventPropogation]")
    __PROPOGATION_DRAG = (By.CSS_SELECTOR,"div[id=dragBox]")
    __DROP_NOT_GREEDY = (By.CSS_SELECTOR,"div[id=notGreedyDropBox]")
    __DROP_GREEDY = (By.CSS_SELECTOR,"div[id=greedyDropBoxInner]")

    __REVERT_TAB = (By.CSS_SELECTOR, "a[id=droppableExample-tab-revertable]")
    __REVERT_DRAG = (By.CSS_SELECTOR, "div[id=revertable]")
    __REVERT_DROP = (By.CSS_SELECTOR,"div[id=revertableDropContainer] div[id=droppable]")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_drop_simple(self):
        drop_element_locator = super()._find(self.__DROP_HERE_FIELD)
        status_before_drag = drop_element_locator.text
        drag_me_element = super()._find(self.__DRUG_ME_SIMPLE)
        super()._scroll_to_element(drag_me_element)
        super()._scroll_to_element(drop_element_locator)
        super()._drag_drop_to_element(drag_me_element, drop_element_locator)
        super()._wait_until_text_is_presented(self.__DROP_HERE_FIELD, "Dropped!")
        status_after_drag = drop_element_locator.text
        return status_before_drag, status_after_drag

    def check_drop_acceptable(self):
        super()._click(self.__ACCEPT_TAB)
        drop_element_locator = super()._find(self.__DROP_HERE_ACCEPTABLE)
        drag_me_element = super()._find(self.__NOT_ACCEPTABLE_DRAG)
        super()._scroll_to_element(drag_me_element)
        super()._scroll_to_element(drop_element_locator)
        super()._drag_drop_to_element(drag_me_element, drop_element_locator)
        status_not_acceptable = drop_element_locator.text
        acceptable_element = super()._find(self.__ACCEPTABLE_DRAG)
        super()._scroll_to_element(acceptable_element)
        super()._scroll_to_element(drop_element_locator)
        super()._drag_drop_to_element(acceptable_element, drop_element_locator)
        super()._wait_until_text_is_presented(self.__DROP_HERE_ACCEPTABLE, "Dropped!")
        status_acceptable = drop_element_locator.text
        return status_not_acceptable, status_acceptable

    def check_drop_propogation(self):
        super()._click(self.___PROPOGATION_TAB)
        drop_element_locator = super()._find(self.__DROP_NOT_GREEDY)
        drag_me_element = super()._find(self.__PROPOGATION_DRAG)
        super()._scroll_to_element(drag_me_element)
        super()._scroll_to_element(drop_element_locator)
        super()._drag_drop_to_element(drag_me_element, drop_element_locator)
        not_greedy_text = drop_element_locator.text
        drop_element_locator = super()._find(self.__DROP_NOT_GREEDY)
        super()._drag_drop_to_element(drag_me_element, drop_element_locator)
        greedy_text = drop_element_locator.text
        return not_greedy_text, greedy_text

    def check_revert_drop(self):
        super()._click(self.__REVERT_TAB)
        drop_element_locator = super()._find(self.__REVERT_DROP)
        drag_me_element = super()._find(self.__REVERT_DRAG)
        super()._scroll_to_element(drag_me_element)
        super()._scroll_to_element(drop_element_locator)
        super()._drag_drop_to_element(drag_me_element, drop_element_locator)
        drop_text = drop_element_locator.text
        time.sleep(3)
        drag_location_after = drag_me_element.location
        return drag_location_after, drop_text

