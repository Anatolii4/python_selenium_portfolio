import time
from datetime import datetime

import allure
import pytest

from pages.widgets.accordian_page import AccordianPage
from pages.widgets.auto_complete_page import AutoCompletePage
from pages.widgets.date_picker_page import DatePickerPage
from pages.widgets.menu_page import MenuPage
from pages.widgets.progress_bar_page import ProgressBarPage
from pages.widgets.select_menu_page import SelectMenuPage
from pages.widgets.slider_page import SliderPage
from pages.widgets.tabs_page import TabsPage
from pages.widgets.tool_tips_page import ToolTipsPage


class TestWidgets:
    @allure.id(1)
    @allure.title("Check three accordians")
    @pytest.mark.smoke
    def test_accordian(self, driver):
        accordian = AccordianPage(driver)
        accordian.open_page()
        section1_title, section1_content = accordian.check_accordions("first")
        assert section1_title == "What is Lorem Ipsum?", "the title of section 1 is incorrect"
        assert len(section1_content) == 574, "the length of section 1 content is incorrect"
        section2_title, section2_content = accordian.check_accordions("second")
        assert section2_title == "Where does it come from?", "the title of section 2 is incorrect"
        assert len(section2_content) == 763, "the length of section 2 content is incorrect"
        section3_title, section3_content = accordian.check_accordions("third")
        assert section3_title == "Why do we use it?", "the title of section 3 is incorrect"
        assert len(section3_content) == 613, "the length of section 3 content is incorrect"

    @allure.id(2)
    @allure.title("Check auto-complete")
    @pytest.mark.smoke
    def test_accordian(self, driver):
        auto_complete = AutoCompletePage(driver)
        auto_complete.open_page()
        selected_value, saved_value = auto_complete.check_auto_complete()

        auto_complete.remove_value()
        number_values_before, number_values_after = auto_complete.remove_value()
        assert selected_value == saved_value, "The value has not been saved"
        assert number_values_before > number_values_after, "Color/s has not been deleted"

    @allure.id(3)
    @allure.title("Check date only")
    @pytest.mark.smoke
    def test_date_picker(self, driver):
        date_picker = DatePickerPage(driver)
        date_picker.open_page()
        saved_date, generated_month, generated_day, generated_year = date_picker.check_date_field()
        generated_date = generated_month, generated_day, generated_year
        formatted_date = f"{datetime.strptime(generated_date[0], '%B').month:02d}/{generated_date[1]:02d}/{generated_date[2]}"
        assert saved_date == formatted_date, "The inputted and saved dates do not match"


    @allure.id(4)
    @allure.title("Check date and time")
    @pytest.mark.smoke
    def test_date_time_picker(self, driver):
        date_picker = DatePickerPage(driver)
        date_picker.open_page()
        date_before, date_after = date_picker.check_time_and_date()
        assert date_before != date_after, "The date and time has not been changed"

    @allure.id(5)
    @allure.title("Check slider")
    @pytest.mark.smoke
    def test_date_time_picker(self, driver):
        slider = SliderPage(driver)
        slider.open_page()
        initial_value, actual_value = slider.check_slider()
        assert initial_value != actual_value, "The bar has not been changed"
    @allure.id(6)
    @allure.title("Check progress bar")
    @pytest.mark.smoke
    def test_date_time_picker(self, driver):
        progress_bar = ProgressBarPage(driver)
        progress_bar.open_page()
        actual_value = progress_bar.check_progress_bar()
        assert actual_value != 0, "Progress bar has not been changed"

    @allure.id(7)
    @allure.title("Check several tabs")
    @pytest.mark.smoke
    def test_date_time_picker(self, driver):
        tabs = TabsPage(driver)
        tabs.open_page()
        result = tabs.check_tab("what")
        result2 = tabs.check_tab("origin")
        result3 = tabs.check_tab("use")
        assert result == 574, "The length of tab 'What' is not as expected"
        assert result2 == 763, "The length of tab 'Origin' is not as expected"
        assert result3 == 613, "The length of tab 'Use' is not as expected"
    @allure.id(8)
    @allure.title("Check button tool tip")
    @pytest.mark.smoke
    def test_tool_tips(self, driver):
        tool_tips = ToolTipsPage(driver)
        tool_tips.open_page()
        button_tip_text = tool_tips.check_tool_tips()
        assert button_tip_text == "You hovered over the Button", "The tool tip has not been shown"

    @allure.id(9)
    @allure.title("Check menus present")
    @pytest.mark.smoke
    def test_menu(self, driver):
        menu = MenuPage(driver)
        menu.open()
        result = menu.check_menu()
        assert result == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], "Some menus are not found"

    def test_select_menu(self, driver):
        select_menu = SelectMenuPage(driver)
        select_menu.open_page()