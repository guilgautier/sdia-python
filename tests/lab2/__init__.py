import numpy as np
import pytest

from lab2.box_window import BoxWindow, UnitBoxWindow


@pytest.fixture
def example_box_window():
    bounds = np.array([[-5, -5], [5, 5]])
    return BoxWindow(bounds)


@pytest.mark.parametrize(
    "point, expected",
    [(np.array([0, 0]), True), (np.array([-1, 5]), True), (np.array([5, 6]), False),],
)
def test_indicator_function_box_2d(example_box_window, point, expected):
    box = example_box_window
    assert box.indicator_function(point) == expected
