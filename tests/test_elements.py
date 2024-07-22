import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.elements_text_box_page import ElementsTextBoxPage
from data.data_generator.general_generator import (
    generate_random_full_name,
    generate_random_email,
    generate_random_current_address,
    generate_random_permanent_address,
)


class TestTextBox:
    def test_submit_form(self, driver):
        text_box = ElementsTextBoxPage(driver)
        text_box.open_page()
        generated_full_name = generate_random_full_name()
        generated_email = generate_random_email()
        generated_current_address = generate_random_current_address()
        generated_current_address = generated_current_address.replace("\n", " ")
        generate_permanent_address = generate_random_permanent_address().replace("\n", " ")
        text_box.fill_form(generated_full_name, generated_email, generated_current_address, generate_permanent_address)
        text_box.submit_form()
        output_full_name, output_email, output_current_address, output_permanent_address = text_box.filed_data()
        assert output_full_name == generated_full_name, "The full name is not as expected"
        assert output_email == generated_email, "The email is not as expected"
        assert output_current_address == generated_current_address, "The current address is not as expected"
        assert output_permanent_address == generate_permanent_address, "The permanent address is not as expected"
