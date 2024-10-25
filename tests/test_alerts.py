import time

import allure
import pytest

from data.data_generator.general_generator import generate_random_full_name
from pages.alerts_frame.alerts_page import AlertsPage
from pages.alerts_frame.browser_window_page import AlertsFramePage


class TestAlertsFrame:
    @allure.id(1)
    @allure.title("Check opening browser's tab")
    @pytest.mark.smoke
    def test_browser_window_new_tab(self, driver):
        browser_window = AlertsFramePage(driver)
        browser_window.open_page()
        new_opened_tab = browser_window.check_opened_new_tab()
        actual_text = browser_window.get_new_tab_text()
        assert new_opened_tab == "https://demoqa.com/sample", 'The new url is not as expected'
        assert actual_text == "This is a sample page", 'The text of new tab is incorrect'

    @allure.id(2)
    @allure.title("Check opening some browser's windows")
    @pytest.mark.smoke
    def test_browser_new_window(self, driver):
        browser_window = AlertsFramePage(driver)
        browser_window.open_page()
        new_opened_window = browser_window.check_opened_new_tab()
        actual_text = browser_window.get_new_tab_text()
        assert new_opened_window == "https://demoqa.com/sample", 'The new url is not as expected'
        assert actual_text == "This is a sample page", 'The text of new tab is incorrect'

    @allure.id(3)
    @allure.title("Check alert")
    @pytest.mark.smoke
    def test_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open_page()
        opened_alert = alerts_page.check_see_alert()
        assert opened_alert == "You clicked a button", "The alert's text is not correct"

    @allure.id(4)
    @allure.title("Check after 5 sec alert")
    @pytest.mark.smoke
    def test_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open_page()
        opened_alert = alerts_page.check_five_sec_alert()
        assert opened_alert == "This alert appeared after 5 seconds", "The alert's text is not correct"

    @allure.id(5)
    @allure.title("Check confirmation box")
    @pytest.mark.smoke
    def test_confirm_box(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open_page()
        opened_alert = alerts_page.check_confirm_box()
        text_result = alerts_page.get_confirm_box_result()
        assert opened_alert == "Do you confirm action?", "The alert's text is not correct"
        assert text_result == "You selected Ok", "The text result is wrong"

    @allure.id(6)
    @allure.title("Check prompt box")
    @pytest.mark.smoke
    def test_confirm_box(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open_page()
        input_text = generate_random_full_name()
        opened_alert = alerts_page.check_prompt_box(input_text)
        text_result = alerts_page.get_prompt_result()
        assert opened_alert == "Please enter your name", "The alert's text is not correct"
        assert text_result == f"You entered {input_text}", "The input text is not as expected"
