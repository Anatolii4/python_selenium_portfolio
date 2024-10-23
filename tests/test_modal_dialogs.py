import time

import allure
import pytest

from pages.alerts_frame.modal_dialogs_page import ModalDialogsPage


class TestModalDialogs:
    @allure.id(1)
    @allure.title("Check two modal windows")
    @pytest.mark.smoke
    def test_modal_dialogs(self, driver):
        modal_dialogs = ModalDialogsPage(driver)
        modal_dialogs.open_page()
        small_modal_result = modal_dialogs.check_small_modal()
        assert small_modal_result == "This is a small modal. It has very less content", "The modal's text is not as expected"
        large_modal_result = modal_dialogs.check_large_modal()
        expected_text = "Lorem Ipsum is simply dummy text of the printing"
        assert expected_text in large_modal_result, "The text of modal window does not match with expected one"