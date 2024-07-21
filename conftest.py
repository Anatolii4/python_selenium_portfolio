import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Opening {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
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
        "--browser", action="store", default="firefox", help="browser to execute tests: chrome or firefox"
    )