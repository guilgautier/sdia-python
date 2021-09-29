import numpy as np
import pytest

from lab2.box_window import BoxWindow, UnitBoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0, 5] x [0, 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [-5, 5], [-1, 9]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0, 5]), True),
        (np.array([2.5, 2.5, 2.5]), True),
        (np.array([-1, 5, 8]), False),
        (np.array([1, 50, 7]), False),
        (np.array([1, 4, 11]), False),
    ],
)
def test_contains(box_2d_05, point, expected):
    is_in = point in box_2d_05
    assert is_in == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 1]]), 1),
        (np.array([[-5, 5], [-10, 20]]), 300),
        (np.array([[-5, 5], [-10, 20], [38.5, 39.5]]), 300),
    ],
)
def test_volume(bounds, expected):
    assert BoxWindow(bounds).volume() == expected


@pytest.mark.parametrize(
    "center, dimension, expected",
    [
        (np.array([0, 0]), 2, np.array(([-0.5, 0.5], [-0.5, 0.5]))),
        (np.array([5, 3]), 2, np.array(([4.5, 5.5], [2.5, 3.5]))),
        (np.array([0, 1, 10]), 3, np.array(([-0.5, 0.5], [0.5, 1.5], [9.5, 10.5]))),
    ],
)
def test_unit_box(center, dimension, expected):
    assert np.array_equal(UnitBoxWindow(center, dimension).bounds, expected)


@pytest.mark.parametrize(
    "bounds, expected",
    [(np.array([[2.5, 3.14], [5, 10], [45, 100]]), np.array([2.82, 7.5, 72.5]))],
)
def test_center(bounds, expected):
    assert np.array_equal(BoxWindow(bounds).center(), expected)
