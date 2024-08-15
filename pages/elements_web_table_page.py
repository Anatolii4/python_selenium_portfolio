import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ElementsWebTablePage(BasePage):
    __URL = "https://demoqa.com/webtables"
    __ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    __CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, "button[class='close']")
    __FIRST_NAME_FILED_LOCATOR = (By.CSS_SELECTOR, "#firstName")
    __LAST_NAME_FILED_LOCATOR = (By.CSS_SELECTOR, "#lastName")
    __EMAIL_FILED_LOCATOR = (By.CSS_SELECTOR, "#userEmail")
    __AGE_FILED_LOCATOR = (By.CSS_SELECTOR, "#age")
    __SALARY_FILED_LOCATOR = (By.CSS_SELECTOR, "#salary")
    __DEPARTMENT_FILED_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='Department']")
    __SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    __SEARCH_FIELD = (By.CSS_SELECTOR, "#searchBox")
    __VERIFIED_DATA = (By.CSS_SELECTOR, "div[class='rt-tr -odd']")
    __DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    __EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        self._open(self.__URL)

    def add_person(self, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
        self._find(self.__ADD_BUTTON).click()
        self._type(self.__FIRST_NAME_FILED_LOCATOR, first_name)
        self._type(self.__LAST_NAME_FILED_LOCATOR, last_name)
        self._type(self.__EMAIL_FILED_LOCATOR, email)
        self._type(self.__AGE_FILED_LOCATOR, age)
        self._type(self.__SALARY_FILED_LOCATOR, salary)
        self._type(self.__DEPARTMENT_FILED_LOCATOR, department)
        return [first_name, last_name, age, email, salary, department]

    def search_created_person(self, key_word: str):
        self._clear_and_type(self.__SEARCH_FIELD, key_word)

    def verify_created_person(self):
        created_person_value = self._find_elements(self.__VERIFIED_DATA)
        created_person_data = []
        for item in created_person_value:
            created_person_data.append(item.text.splitlines())
        return created_person_data[0]

    def delete_person(self):
        self._find(self.__DELETE_BUTTON).click()

    def is_person_deleted(self) -> bool:
        return self._wait_until_element_is_not_presented(self.__VERIFIED_DATA)

    def edit_person_info(self, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
        self._find(self.__EDIT_BUTTON).click()
        super()._clear_and_type(self.__FIRST_NAME_FILED_LOCATOR, first_name)
        super()._clear_and_type(self.__LAST_NAME_FILED_LOCATOR, last_name)
        super()._clear_and_type(self.__EMAIL_FILED_LOCATOR, email)
        super()._clear_and_type(self.__AGE_FILED_LOCATOR, age)
        super()._clear_and_type(self.__SALARY_FILED_LOCATOR, salary)
        super()._clear_and_type(self.__DEPARTMENT_FILED_LOCATOR, department)
        return [first_name, last_name, age, email, salary, department]

    def submit_changes(self):
        self._click(self.__SUBMIT_BUTTON)

    def close_pop_up(self):
        self._find(self.__CLOSE_POPUP_BUTTON).click()
