import time

import allure
import pytest

from pages.interactions.draggable_page import DraggablePage
from pages.interactions.droppable_page import DroppablePage
from pages.interactions.resizable_page import ResizablePage
from pages.interactions.selectable_page import SelectablePage
from pages.interactions.sortable_page import SortablePage


class TestInteractions:
    @allure.id(1)
    @allure.title("Check sortable elements")
    @pytest.mark.smoke
    @pytest.mark.xfail()
    def test_sortable(self, driver):

        sortable = SortablePage(driver)
        sortable.open_page()
        list_order_before, list_order_after = sortable.change_sort_of_list()
        assert list_order_before != list_order_after, "Sort of list has not been applyed"

        grid_order_before, grid_order_after = sortable.change_sort_of_grid()
        assert grid_order_before != grid_order_after, "Sort of grid has not been applyed"

    @allure.id(2)
    @allure.title("Check selectable elements")
    @pytest.mark.smoke
    def test_selectable(self, driver):
        selectable = SelectablePage(driver)
        selectable.open_page()
        number_active_list_items = selectable.select_list_items()
        assert number_active_list_items == 2, "The elements of the list were not clicked"
        number_active_grid_items = selectable.select_grid_items()
        assert number_active_grid_items == 2, "The elements of the grid were not clicked"

    @allure.id(3)
    @allure.title("Check resizable elements")
    @pytest.mark.smoke
    @pytest.mark.xfail
    def test_selectable(self, driver):
        resizable = ResizablePage(driver)
        resizable.open_page()
        box_size = resizable.change_resizable_box()
        assert box_size == ('300', '300'), "the box size has not been changed"
        resizable_size = resizable.change_resizable()
        assert resizable_size == ('100', '50'), "the resizable size has not been changed"

    @allure.id(4)
    @allure.title("Check some droppable elements")
    @pytest.mark.smoke
    @pytest.mark.xfail
    def test_droppable(self, driver):
        droppable = DroppablePage(driver)
        droppable.open_page()
        status_before, status_after = droppable.check_drop_simple()
        assert status_before != status_after, "The element has not been dropped"
        not_acceptable_text, acceptable_text = droppable.check_drop_acceptable()
        assert not_acceptable_text == "Drop here", "The item was acceptable, but should not be"
        assert acceptable_text == "Dropped!", "The item was not acceptable, but should be"
        # not_greedy_text, greedy_text = droppable.check_drop_propogation()
        # assert not_greedy_text == "Outer droppable\nInner droppable (not greedy)", "Fail to drop to Not greedy area"
        # assert greedy_text == "Dropped!\nDropped!", "Fail to drop to Not greedy area"
        current_position, status = droppable.check_revert_drop()
        assert status == "Dropped!", "The item has not been dropped in a proper place"
        assert current_position == {'x': 552, 'y': 588}, "the item has not been reverted to the initial position"

    @allure.id(5)
    @allure.title("Check some draggable elements")
    @pytest.mark.smoke

    def test_droppable(self, driver):
        draggable = DraggablePage(driver)
        draggable.open_page()
        initial_location, final_location = draggable.check_drag_simple()
        assert initial_location != final_location, "The 'drag me' element has not been moved"
        y_location = draggable.check_x_axis_restricted()
        assert y_location == "top: 0", "the Y position has been changed"
        x_location = draggable.check_y_axis_restricted()
        assert x_location == ['0'], "the X position has been changed"