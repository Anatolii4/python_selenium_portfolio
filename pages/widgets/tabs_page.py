from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class TabsPage(BasePage):
    __URL = "https://demoqa.com/tabs"
    __WHAT_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-what]")
    __WHAT_TAB_CONTENT = (By.CSS_SELECTOR, "div[id=demo-tabpane-what] > p")
    __ORIGIN_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-origin]")
    __ORIGIN_TAB_CONTENT = (By.CSS_SELECTOR, "div[id=demo-tabpane-origin] > p")
    __USE_TAB = (By.CSS_SELECTOR, "a[id=demo-tab-use]")
    __USE_TAB_CONTENT = (By.CSS_SELECTOR, "div[id=demo-tabpane-use] > p")
    __USE_MORE = (By.CSS_SELECTOR, "a[id=demo-tab-more]")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_tab(self, tab_name: str):
        tab_data = {
            "origin": {"tab": self.__ORIGIN_TAB, "content": self.__ORIGIN_TAB_CONTENT},
            "use": {"tab": self.__USE_TAB, "content": self.__USE_TAB_CONTENT},
            "what": {"content": self.__WHAT_TAB_CONTENT}
        }
        if tab_name in tab_data:
            if tab_name != "what":
                tab_locator = super()._find(tab_data[tab_name]["tab"])
                super()._scroll_to_element(tab_locator)
                tab_locator.click()
            tab_text = super()._get_text(tab_data[tab_name]["content"])
            return len(tab_text)


