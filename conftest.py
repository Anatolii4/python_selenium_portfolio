import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.data_generator.general_generator import generate_random_first_name, generate_random_last_name, \
    generate_random_email, generate_random_age, generate_random_salary, generate_random_department
from pages.elements_pages.elements_web_table_page import ElementsWebTablePage


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Opening {browser} driver")
    if browser == "chrome":
        options = Options()
        # options.add_argument("--headless")
        my_driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Expected chrome or firefox but got {browser}")
    my_driver.maximize_window()
    yield my_driver
    print("Closing driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests: chrome or firefox"

    )


@pytest.fixture()
def create_person(driver):
    web_table = ElementsWebTablePage(driver)
    web_table.open_page()
    person_first_name = generate_random_first_name()
    person_last_name = generate_random_last_name()
    person_email = generate_random_email()
    person_age = generate_random_age()
    person_salary = generate_random_salary()
    person_department = generate_random_department()
    web_table.add_person(person_first_name, person_last_name, person_email, person_age,
                         person_salary, person_department)
    web_table.submit_changes()
    web_table.search_created_person(person_first_name)
    yield
    web_table.delete_person()

