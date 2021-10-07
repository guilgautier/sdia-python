import numpy as np
import pytest

from lab2.box_window import BoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        ([[2.5, 2.5]], "BoxWindow: [2.5, 2.5]"),
        ([[0, 5], [0, 5]], "BoxWindow: [0, 5] x [0, 5]"),
        (
            [[0, 5], [-1.45, 3.14], [-10, 10]],
            "BoxWindow: [0, 5] x [-1.45, 3.14] x [-10, 10]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected


@pytest.fixture
def example_box_window():
    bounds = [[-5, 5], [-5, 5]]
    return BoxWindow(bounds)


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0]], [True]),
        ([[-1, 5], [1, 2]], [True, True]),
        ([[5, 6], [1, 2], [5, 6]], [False, True, False]),
    ],
)
def test_indicator_function(example_box_window, points, expected):
    box = example_box_window
    assert (box.indicator_function(points)) == expected


@pytest.mark.parametrize(
    "box, expected",
    [
        (BoxWindow([[0, 1]]), [0.5]),
        (BoxWindow([[1, 2], [0, 2]]), [1.5, 1]),
        (BoxWindow([[0, -4], [4, 5], [1, 3]]), [-2, 4.5, 2]),
        (BoxWindow([[1, 2], [0, 2], [-4, 4], [1, 2]]), [1.5, 1, 0, 1.5]),
    ],
)
def test_center(box, expected):
    assert box.center() == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================
