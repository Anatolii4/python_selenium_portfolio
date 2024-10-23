from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    __URL = "https://demoqa.com/nestedframes"
    __PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id=frame1]")
    __PARENT_TITLE = (By.CSS_SELECTOR, "body")
    __CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    __CHILD_TITLE = (By.CSS_SELECTOR, "p")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_nested_frames(self):
        parent_frame = super()._find(self.__PARENT_FRAME)
        super()._switch_to_frame(parent_frame)
        parent_text = super()._get_text(self.__PARENT_TITLE)
        child_frame = super()._find(self.__CHILD_FRAME)
        super()._switch_to_frame(child_frame)
        child_text = super()._get_text(self.__CHILD_TITLE)
        return parent_text, child_text