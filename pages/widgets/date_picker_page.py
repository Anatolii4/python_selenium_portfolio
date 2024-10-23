import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from data.data_generator.general_generator import generate_random_month_birth, generate_random_year_birth
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    __URL = "https://demoqa.com/date-picker"
    __DATE_INPUT_FIELD = (By.CSS_SELECTOR, "input[id=datePickerMonthYearInput]")
    __MONTH_PICKER = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    __CHOOSE_MONTH = "//option[text()='{}']"
    __YEAR_PICKER = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    __CHOOSE_YEAR = "//option[text()='{}']"
    __CHOOSE_DAY = "//div[contains(@class, 'react-datepicker__day') and text()='{}']"

    __TIME_DATE_INPUT_FIELD = (By.CSS_SELECTOR, "input[id=dateAndTimePickerInput]")
    __MONTH_PICKER2 = (By.CSS_SELECTOR, "div[class=react-datepicker__month-read-view]")
    __CHOOSE_MONTH2 = "//div[text()='{}']"
    __YEAR_PICKER2 = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    __CHOOSE_YEAR2 = "//div[text()='{}']"
    __CHOOSE_DAY2 = "//div[@class='react-datepicker__day react-datepicker__day--{}']"
    __TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_page(self):
        super()._open(self.__URL)

    def check_date_field(self):
        input_field = super()._find(self.__DATE_INPUT_FIELD)
        super()._scroll_to_element(input_field)
        input_field.click()
        super()._click(self.__MONTH_PICKER)
        generated_month = generate_random_month_birth()
        pick_month = (By.XPATH, self.__CHOOSE_MONTH.format(generated_month))
        super()._click(pick_month)

        super()._click(self.__YEAR_PICKER)
        generated_year = generate_random_year_birth()
        pick_year = (By.XPATH, self.__CHOOSE_YEAR.format(generated_year))
        super()._click(pick_year)

        generated_day = random.randint(1, 28)
        picked_day = (By.XPATH, self.__CHOOSE_DAY.format(generated_day))
        super()._click(picked_day)
        saved_date = super()._find(self.__DATE_INPUT_FIELD).get_attribute('value')
        return saved_date, generated_month, generated_day, generated_year

    def check_time_and_date(self):
        input_field = super()._find(self.__TIME_DATE_INPUT_FIELD)
        saved_date_before = input_field.get_attribute("value")
        super()._scroll_to_element(input_field)
        input_field.click()
        super()._click(self.__MONTH_PICKER2)
        generated_month = generate_random_month_birth()
        pick_month = (By.XPATH, self.__CHOOSE_MONTH2.format(generated_month))
        super()._click(pick_month)

        super()._click(self.__YEAR_PICKER2)
        pick_year = (By.XPATH, self.__CHOOSE_YEAR2.format(random.randint(2019, 2029)))
        super()._click(pick_year)

        generated_day = random.randint(1, 28)
        formatted_day = f'{generated_day:03}'
        picked_day = (By.XPATH, self.__CHOOSE_DAY2.format(formatted_day))
        super()._click(picked_day)
        self.select_time_item_from_list()
        saved_date_after = input_field.get_attribute("value")
        return saved_date_before, saved_date_after

    def select_time_item_from_list(self):
        time_list = super()._find_elements(self.__TIME_LIST)
        picked_time = random.sample(time_list, 1)[0]
        super()._scroll_to_element(picked_time)
        picked_time.click()
