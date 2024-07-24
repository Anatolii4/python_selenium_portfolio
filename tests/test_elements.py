import time

import allure

from pages.elements_checkbox_page import ElementsCheckBoxPage
from pages.elements_text_box_page import ElementsTextBoxPage
from data.data_generator.general_generator import (
    generate_random_full_name,
    generate_random_email,
    generate_random_current_address,
    generate_random_permanent_address,
)


class TestElements:
    @allure.id(1)
    @allure.title("Test some fields")
    def test_text_box_form(self, driver):
        """
        Submit the form
        Check the filled data
        """
        text_box = ElementsTextBoxPage(driver)

        with allure.step("Open text box page"):
            text_box.open_page()

        with allure.step("Fill required data and submit the form"):
            generated_full_name = generate_random_full_name()
            generated_email = generate_random_email()
            generated_current_address = generate_random_current_address()
            generated_current_address = generated_current_address.replace("\n", " ")
            generate_permanent_address = generate_random_permanent_address().replace("\n", " ")
            text_box.fill_form(generated_full_name, generated_email, generated_current_address,
                               generate_permanent_address)
            text_box.submit_form()

            with allure.step("Check filled data"):
                output_full_name, output_email, output_current_address, output_permanent_address = text_box.filed_data()
                assert output_full_name == generated_full_name, "The full name is not as expected"
                assert output_email == generated_email, "The email is not as expected"
                assert output_current_address == generated_current_address, "The current address is not as expected"
                assert output_permanent_address == generate_permanent_address, "The permanent address is not as expected"

    @allure.id(2)
    @allure.title("Checking some check boxes")
    def test_checkbox_form(self, driver):
        checkbox_page = ElementsCheckBoxPage(driver)
        with allure.step("Open text box page"):
            checkbox_page.open_page()

        with allure.step("Check random checkbox"):
            checkbox_page.expand_full_list()
            checkbox_page.click_random_num_checkboxes()
            #time.sleep(5)
            clicked_boxes = checkbox_page.get_titles_of_checked_boxes()
            output_result = checkbox_page.get_output_result()
            assert clicked_boxes == output_result, "The output does not match clicked checkboxes"
