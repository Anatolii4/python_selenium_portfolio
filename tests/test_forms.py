import time

import pytest

from data.data_generator.general_generator import *
import allure

from pages.forms_page.form_page import FormsPage


class TestFormsPage:

    @allure.id(1)
    @allure.title("Check full form ")
    @pytest.mark.smoke
    def test_forms_page(self, driver):
        forms_page = FormsPage(driver)
        with allure.step("Open student registration form"):
            forms_page.open_page()
        with allure.step("Fill in First name and Last name"):
            generated_first_name = generate_random_first_name()
            generated_last_name = generate_random_last_name()
            generated_full_name = generated_first_name + " " + generated_last_name
            forms_page.input_full_name(generated_first_name, generated_last_name)
        with allure.step("Fill in email"):
            email = generate_random_email()
            forms_page.input_email(email)
        with allure.step("Fill in gender"):
            gender = "Male"
            forms_page.click_gender(gender)
        with allure.step("Fill in phone number"):
            phone_number = str(random.randint(1000000000, 9999999999))
            forms_page.input_phone_number(phone_number)
        with allure.step("Fill in date of birth"):
            dob = forms_page.choose_date_of_birth()
            formatted_date = f"{dob[0]:02d} {dob[1]},{dob[2]}"
        with allure.step("Choose any subject"):
            subject = forms_page.choose_subject()
        with allure.step("Choose any hobbies"):
            hobbies = ", ".join(forms_page.choose_hobbies())
        with allure.step("Upload the file"):
            path = generate_file()
            file_name = path.split("\\")[-1]
            forms_page.upload_file(path)
        with allure.step("Fill in the address"):
            address = forms_page.input_current_address()
        with allure.step("Choose state and city"):
            state_city = ", ".join(forms_page.choose_state_and_city()).replace(",", "")
        with allure.step("Submit the form"):
            forms_page.submit_form()
            with allure.step("Check submitted full name"):
                assert generated_full_name == forms_page.check_submitted_info()[0], "The student full name is not as expected"
            with allure.step("Check submitted email"):
                assert email == forms_page.check_submitted_info()[1], "The submitted email is not as expected"
            with allure.step("Check submitted gender"):
                assert gender == forms_page.check_submitted_info()[2], "The submitted gender is not as expected"
            with allure.step("Check submitted phone number"):
                assert phone_number == forms_page.check_submitted_info()[3], "The submitted phone is not as expected"
            with allure.step("Check submitted date of birth"):
                assert formatted_date == forms_page.check_submitted_info()[4], "The submitted dob is not as expected"
            with allure.step("Check submitted subject"):
                assert subject == forms_page.check_submitted_info()[5], "The submitted subject is not as expected"
            with allure.step("Check submitted hobbies"):
                assert hobbies == forms_page.check_submitted_info()[6], "The submitted hobbies are not as expected"
            with allure.step("Check submitted file name"):
                assert file_name == forms_page.check_submitted_info()[7], "The submitted file is not as expected"
            with allure.step("Check submitted address"):
                assert address == forms_page.check_submitted_info()[8], "The current address is not as expected"
            with allure.step("Check submitted state and city"):
                assert state_city == forms_page.check_submitted_info()[9], "The expected state and city are not as expected"