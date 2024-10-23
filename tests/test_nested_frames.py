import allure
import pytest

from pages.alerts_frame.nested_frames_page import NestedFramesPage


class TestNestedFrames:

    @allure.id(1)
    @allure.title("Check two nested frames")
    @pytest.mark.smoke
    def test_nested_frames(self, driver):
        nested_frames = NestedFramesPage(driver)
        nested_frames.open_page()
        parent_text, child_text = nested_frames.check_nested_frames()
        assert parent_text == "Parent frame", "The parent frame is not exist"
        assert child_text == "Child Iframe", "The child frame is not exist"

