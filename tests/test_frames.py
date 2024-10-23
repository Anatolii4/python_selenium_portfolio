import allure
import pytest

from pages.alerts_frame.frame_page import FramePage


class TestFrames:
    @allure.id(1)
    @allure.title("Check two test frames")
    @pytest.mark.smoke
    def test_frames(self, driver):
        frames = FramePage(driver)
        frames.open_page()
        frame1_result = frames.check_frame("frame1")
        frame2_result = frames.check_frame("frame2")
        assert frame1_result == ['500px', '350px', 'This is a sample page'], "The frame1 parameters are wrong"
        assert frame2_result == ['100px', '100px', 'This is a sample page'], "The frame2 parameters are wrong"
