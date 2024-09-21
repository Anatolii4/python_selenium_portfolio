import pytest

from data.data_generator.general_generator import *
import allure

from pages.elements_pages.dynamic_properties_page import DynamicPropertiesPage
from pages.elements_pages.elements_buttons_page import ElementsButtonsPage
from pages.elements_pages.elements_checkbox_page import ElementsCheckBoxPage
from pages.elements_pages.elements_links_page import ElementsLinksPage
from pages.elements_pages.elements_radio_button_page import ElementsRadioButtonPage
from pages.elements_pages.elements_text_box_page import ElementsTextBoxPage

from pages.elements_pages.elements_web_table_page import ElementsWebTablePage
from pages.elements_pages.upload_download_page import UploadDownloadPage


class TestElements:
    @allure.id(1)
    @allure.title("Test some fields")
    @pytest.mark.smoke
    @pytest.mark.regression
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
    @pytest.mark.smoke
    def test_checkbox_form(self, driver):
        checkbox_page = ElementsCheckBoxPage(driver)
        with allure.step("Open text box page"):
            checkbox_page.open_page()

        with allure.step("Check random checkbox"):
            checkbox_page.expand_full_list()
            checkbox_page.click_random_num_checkboxes()
            clicked_boxes = checkbox_page.get_titles_of_checked_boxes()
            output_result = checkbox_page.get_output_result()
            assert clicked_boxes == output_result, "The output does not match clicked checkboxes"

    @allure.id(3)
    @allure.title("Checking radio buttons")
    @pytest.mark.smoke
    def test_radio_button_form(self, driver):
        radio_button = ElementsRadioButtonPage(driver)
        with allure.step("Open text box page"):
            radio_button.open_page()

        with allure.step("Click random button"):
            clicked_button = radio_button.click_random_radio_button()

            with allure.step("Check that clicked button reflected in the output section"):
                output_result = radio_button.get_output_result()
            assert clicked_button == output_result, "Clicked button does not reflected in output section"

    @allure.id(4)
    @allure.title("Adding new person into the table")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_web_table_add_person(self, driver):
        web_table = ElementsWebTablePage(driver)
        with allure.step("Open web table page"):
            web_table.open_page()

        with allure.step("Add new person into the table"):
            person_first_name = generate_random_first_name()
            person_last_name = generate_random_last_name()
            person_email = generate_random_email()
            person_age = generate_random_age()
            person_salary = generate_random_salary()
            person_department = generate_random_department()
            generated_person = web_table.add_person(person_first_name, person_last_name, person_email, person_age,
                                                    person_salary, person_department)
            web_table.submit_changes()
        with allure.step("Try to search a newly added person"):
            web_table.search_created_person(person_first_name)

            with allure.step("Verify the data reflected in the table"):
                output_result = web_table.verify_created_person()
                assert generated_person == output_result, "added person is not reflected in the table"

    @allure.id(5)
    @allure.title("Delete a person from a table")
    @pytest.mark.smoke
    def test_web_table_delete_person(self, driver):
        web_table = ElementsWebTablePage(driver)
        with allure.step("Open web table page"):
            web_table.open_page()

        with allure.step("Add new person into the table"):
            person_first_name = generate_random_first_name()
            person_last_name = generate_random_last_name()
            person_email = generate_random_email()
            person_age = generate_random_age()
            person_salary = generate_random_salary()
            person_department = generate_random_department()
            web_table.add_person(person_first_name, person_last_name, person_email, person_age,
                                 person_salary, person_department)
            web_table.submit_changes()

            with allure.step("Try to search a newly added person"):
                web_table.search_created_person(person_first_name)

            with allure.step("Delete a created person"):
                web_table.delete_person()

                with allure.step("Verify deleted person"):
                    assert web_table.is_person_deleted(), "Person is not deleted"

    @allure.id(6)
    @allure.title("Edit person's information")
    @pytest.mark.smoke
    def test_edit_person(self, create_person, driver):
        web_table = ElementsWebTablePage(driver)

        with allure.step("Edit existing person"):
            person_first_name = generate_random_first_name()
            person_last_name = generate_random_last_name()
            person_email = generate_random_email()
            person_age = generate_random_age()
            person_salary = generate_random_salary()
            person_department = generate_random_department()
            edited_person = web_table.edit_person_info(person_first_name, person_last_name, person_email, person_age,
                                                       person_salary, person_department)
            web_table.submit_changes()
        with allure.step("Try to search an edited person"):
            web_table.search_created_person(person_first_name)

            with allure.step("Verify the data reflected in the table"):
                output_result = web_table.verify_created_person()
                assert edited_person == output_result, "edited person is not reflected in the table"

    @allure.id(7)
    @allure.title("Test different buttons")
    @pytest.mark.smoke
    def test_button_page(self, driver):
        buttons_page = ElementsButtonsPage(driver)
        with allure.step("Open button page"):
            buttons_page.open_page()
        with allure.step("Click different buttons"):
            buttons_page.click_on_different_way("double")
            buttons_page.click_on_different_way("right")
            buttons_page.click_on_different_way("click")

    @allure.id(8)
    @allure.title("Test different links")
    @pytest.mark.smoke
    def test_check_link(self, driver):
        links_page = ElementsLinksPage(driver)
        with allure.step("Open links page"):
            links_page.open_page()
            with allure.step("Verify newly opened URL"):
                actual_url = links_page.check_new_tab_is_open()
                assert actual_url == "https://demoqa.com/", "URL is not as expected"

    @allure.id(9)
    @allure.title("Test different links")
    @pytest.mark.smoke
    def test_broken_link(self, driver):
        links_page = ElementsLinksPage(driver)
        with allure.step("Open links page"):
            links_page.open_page()
            with allure.step("Verify response of the link"):
                actual_status_code = links_page.check_api_request_link()
                assert links_page.check_api_request_link() == 400, f"The status code is {actual_status_code}, but should be 400"

    @allure.id(10)
    @allure.title("Download and Upload files")
    @pytest.mark.smoke
    def test_upload_file(self, driver):
        upload_download_page = UploadDownloadPage(driver)
        with allure.step("Open upload/download page"):
            upload_download_page.open_page()
            path = generate_file()
        with allure.step("Upload file"):
            upload_download_page.upload_file(path)
            uploaded_path = upload_download_page.actual_uploaded_path()
            with allure.step("Check uploaded file"):
                expected_file_name = path.split("\\")[-1]
                assert uploaded_path.endswith(expected_file_name), "The path of uploaded file is not as expected"
        with allure.step("Udelete created file"):
            upload_download_page.remove_generated_file(path)

    def test_download_file(self, driver):
        upload_download_page = UploadDownloadPage(driver)
        with allure.step("Open upload/download page"):
            upload_download_page.open_page()
        with allure.step("Open upload/download page"):
            upload_download_page.download_file()

    @allure.id(11)
    @allure.title("Dynamic properties")
    @pytest.mark.smoke
    def test_color_button(self, driver):
        properties_page = DynamicPropertiesPage(driver)
        with allure.step("Open Dynamic properties page"):
            properties_page.open_page()
            with allure.step("Check button changed color after 5 seconds"):
                assert properties_page.check_color_change_button() != "rgba(255, 255, 255, 1)", ("The color has not "
                                                                                                 "been changed")

    def test_invisible_button(self, driver):
        properties_page = DynamicPropertiesPage(driver)
        with allure.step("Open Dynamic properties page"):
            properties_page.open_page()
            with allure.step("Check button became visible after 5 seconds"):
                properties_page.check_invisible_button()
