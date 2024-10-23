import os
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from data.data_generator.general_generator import generate_random_month_birth, generate_random_year_birth, \
    generate_random_subject, generate_random_current_address, generate_random_state, choose_random_city
from pages.base_page import BasePage


class FormsPage(BasePage):
    __URL = "https://demoqa.com/automation-practice-form"
    __FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[id=firstName]")
    __LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[id=lastName]")
    __EMAIL_FIELD = (By.CSS_SELECTOR, "input[id=userEmail]")
    __GENDER_RADIO_BUTTON = "//label[text()='{}']"
    __MOBILE_FIELD = (By.CSS_SELECTOR, "input[id=userNumber]")
    __DATE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "input[id=dateOfBirthInput]")
    __SUBJECTS_FIELD = (By.CSS_SELECTOR, "input[id=subjectsInput]")
    __HOBBIES = (By.CSS_SELECTOR, "div[class='custom-control custom-checkbox custom-control-inline']")
    __UPLOAD_PICTURE = (By.CSS_SELECTOR, "input[id=uploadPicture]")
    __CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id=currentAddress]")
    __MONTH_PICKER = (By.CLASS_NAME, 'react-datepicker__month-select')
    __CHOOSE_MONTH = "//option[text()='{}']"
    __YEAR_PICKER = (By.CLASS_NAME, 'react-datepicker__year-select')
    __CHOOSE_YEAR = "//option[text()='{}']"
    __CHOOSE_DAY = "//div[contains(@class, 'react-datepicker__day') and text()='{}']"
    __STATE_FIELD = (By.CSS_SELECTOR, "#state")
    __CHOOSE_STATE = "//div[text()='{}']"
    __CHOOSE_CITY = "//div[text()='{}']"
    __CITY_FIELD = (By.CSS_SELECTOR, "#city")
    __SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id=submit]")

    __SUBMITTED_FORM = (By.XPATH, "//div[@class='table-responsive']//td[2]")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def input_full_name(self, first_name: str, last_name: str):
        super()._find(self.__FIRST_NAME_FIELD).send_keys(first_name)
        super()._find(self.__LAST_NAME_FIELD).send_keys(last_name)

    def input_email(self, email: str):
        super()._find(self.__EMAIL_FIELD).send_keys(email)

    def click_gender(self, gender: str):
        gender_locator = (By.XPATH, self.__GENDER_RADIO_BUTTON.format(gender))
        super()._click(gender_locator)

    def input_phone_number(self, number: str):
        super()._find(self.__MOBILE_FIELD).send_keys(number)

    def choose_date_of_birth(self):
        dob = super()._find(self.__DATE_OF_BIRTH_FIELD).click()
        super()._scroll_to_element(dob)
        super()._find(self.__MONTH_PICKER).click()
        generated_month = generate_random_month_birth()
        month_locator = (By.XPATH, self.__CHOOSE_MONTH.format(generated_month))
        super()._click(month_locator)

        super()._find(self.__YEAR_PICKER).click()
        generated_year = generate_random_year_birth()
        year_locator = (By.XPATH, self.__CHOOSE_YEAR.format(generated_year))
        super()._click(year_locator)

        generated_day = random.randint(1, 28)
        day_locator = (By.XPATH, self.__CHOOSE_DAY.format(generated_day))
        super()._click(day_locator)
        return generated_day, generated_month, generated_year
    def choose_subject(self):
        generate_subject = generate_random_subject()
        subject = super()._find(self.__SUBJECTS_FIELD).send_keys(generate_subject)
        super()._find(self.__SUBJECTS_FIELD).send_keys(Keys.ENTER)
        return generate_subject
    def choose_hobbies(self):
        hobbies_list = super()._find_elements(self.__HOBBIES)
        items_to_click = random.sample(hobbies_list, random.randint(1, 3))
        chose_hobbies = []
        for item in items_to_click:
            chose_hobbies.append(item.text)
            self._scroll_to_element(item)
            item.click()
        return chose_hobbies
    def upload_file(self, path):
        super()._find(self.__UPLOAD_PICTURE).send_keys(path)
        os.remove(path)

    def input_current_address(self):
        generated_address = generate_random_current_address()
        cleared_address = generated_address.replace("\n", "")
        super()._find(self.__CURRENT_ADDRESS).send_keys(cleared_address)
        return cleared_address

    def choose_state_and_city(self):
        state_field = super()._find(self.__STATE_FIELD)
        super()._scroll_to_element(state_field)
        super()._click(self.__STATE_FIELD)
        generated_state = generate_random_state()
        state_locator = (By.XPATH, self.__CHOOSE_STATE.format(generated_state))
        super()._click(state_locator)

        city_field = super()._find(self.__CITY_FIELD)
        super()._scroll_to_element(city_field)
        super()._click(self.__CITY_FIELD)
        generated_city = choose_random_city(generated_state)
        city_locator = (By.XPATH, self.__CHOOSE_CITY.format(generated_city))
        super()._click(city_locator)
        return generated_state, generated_city
    def submit_form(self):
        super()._click(self.__SUBMIT_BUTTON)

    def check_submitted_info(self):
        result_list = super()._find_elements(self.__SUBMITTED_FORM)
        data = []
        for item in result_list:
            data.append(item.text)
        return data