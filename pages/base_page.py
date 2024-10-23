import time
from typing import List

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure
from allure_commons.types import AttachmentType


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _open(self, url: str):
        with allure.step("Open url"):
            self.driver.get(url)

    def _wait_until_element_is_visible(self, locator: tuple, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_elements_are_visible(self, locator: tuple, timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.visibility_of_all_elements_located(locator))

    def _wait_until_element_is_present(self, locator: tuple, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.presence_of_element_located(locator))

    def _wait_until_elements_are_present(self, locator: tuple, timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.presence_of_all_elements_located(locator))
    def _wait_until_element_is_clickable(self, locator: tuple, timeout: int =5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_until_element_is_not_presented(self, locator: tuple, timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.presence_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    def _wait_until_text_is_presented(self, locator: tuple, text: str, timeout: int = 3 ):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.text_to_be_present_in_element(locator, text))


    def _scroll_to_element(self, element):
        with allure.step("Scroll to the element"):
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    def _find(self, locator: tuple) -> WebElement:
        with allure.step("Find element"):
            self._wait_until_element_is_visible(locator)
            return self.driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> list[WebElement]:
        with allure.step("Find element"):
            self._wait_until_elements_are_visible(locator)
            return self.driver.find_elements(*locator)

    def _click(self, locator: tuple):
        with allure.step("Click the element"):
            self._wait_until_element_is_clickable(locator)
            self._find(locator).click()

    def _type(self, locator: tuple, text: str):
        with allure.step("Type some text"):
            self._find(locator).send_keys(text)

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text

    def _get_current_url(self) -> str:
        return self.driver.current_url

    def _make_screenshot(self, screenshot_name):
        allure.attach(body=self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=AttachmentType.PNG)

    def _clear_and_type(self, locator: tuple, text: str):
        self._find(locator).clear()
        self._find(locator).send_keys(text)

    def _double_click(self, element: WebElement):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def _right_click(self, element: WebElement):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def _switch_to_new_tab(self):
        list_of_tabs = self.driver.window_handles
        self.driver.switch_to.window(list_of_tabs[-1])

    def _switch_to_allert(self, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.alert_is_present())
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def _confirm_alert(self, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.alert_is_present())
        alert_window = self.driver.switch_to.alert
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    def _prompt_alert(self, text: str, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.alert_is_present())
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_txt = alert_window.text
        alert_window.accept()
        return alert_txt

    def _switch_to_frame(self, frame: WebElement):
        self.driver.switch_to.frame(frame)

    def _switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def _drag_and_drop_by_offset(self, element:WebElement, x_cords, y_cords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_cords, y_cords)
        action.perform()

    def _hover_and_get_text(self, hover_element: tuple, wait_element: tuple, tool_tip_text: tuple):
        element = self._find(hover_element)
        self._scroll_to_element(element)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        self._wait_until_element_is_visible(wait_element)
        tool_tip_text = self._find(tool_tip_text).text
        return tool_tip_text

    def _move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def _wait_until_menu_are_present(self, locator: tuple, timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(ec.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def _drag_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()