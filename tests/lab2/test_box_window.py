import numpy as np
import pytest

from lab2.box_window import BoxWindow, UnitBoxWindow


def test_raise_type_error_when_points_is_not_an_array():
    with pytest.raises(AssertionError):
        # call_something_that_raises_TypeError()
        L = [[1, 2], [3, 4]]
        box = BoxWindow(L)
        raise AssertionError()


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
def test_box_string_resentation(bounds, expected):
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


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.__contains__(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


@pytest.mark.parametrize(
    "box, expected",
    [
        (np.array([[1, 2]]), 1),
        (np.array([[1, 2], [3, 4]]), 2),
        (np.array([[1, 2], [3, 4], [5, 6]]), 3),
        (np.array([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]]), 6),
    ],
)
def test_len_box(box, expected):
    assert len(BoxWindow(box)) == expected


@pytest.mark.parametrize(
    "box, expected",
    [
        (np.array([[1, 2]]), 1),
        (np.array([[1, 2], [3, 4]]), 2),
        (np.array([[1, 2], [3, 4], [5, 6]]), 3),
        (np.array([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]]), 6),
    ],
)
def test_dimension_box(box, expected):
    assert BoxWindow(box).dimension() == expected


@pytest.mark.parametrize(
    "box, expected",
    [
        (np.array([[1, 2]]), 1),
        (np.array([[1, 3], [3, 5]]), 4),
        (np.array([[1, 2], [3, 4], [5, 7]]), 2),
        (np.array([[1, 2], [3, 5], [5, 9], [1, 2], [3, 5], [5, 6]]), 16),
    ],
)
def test_volume_box(box, expected):
    assert BoxWindow(box).volume() == expected


def test_rand_onepoint_onedimension():
    box = BoxWindow(np.array([[1, 2]]))
    assert box.__contains__(box.rand()[0])


def test_rand_multiplepoint_3dimension():
    box = BoxWindow(np.array([[1, 2], [10, 15.5], [3.5, 7]]))
    coord = box.rand(100)
    for value in coord:
        assert box.__contains__(value)


@pytest.mark.parametrize(
    "dimension, expected",
    [
        (1, "BoxWindow: [-0.5, 0.5]"),
        (2, "BoxWindow: [-0.5, 0.5] x [-0.5, 0.5]"),
        (
            3,
            "BoxWindow: [-0.5, 0.5] x [-0.5, 0.5] x [-0.5, 0.5]",
        ),
    ],
)
def test_UnitBoxWindow(dimension, expected):
    unitBox = UnitBoxWindow(dimension)
    assert unitBox.__str__() == expected


@pytest.mark.parametrize(
    "dimension, center, expected",
    [
        (1, np.array([2.5]), "BoxWindow: [2.0, 3.0]"),
    ],
)
def test_UnitBoxWindow_with_center_specified(dimension, center, expected):
    unitBox = UnitBoxWindow(dimension, center)
    assert unitBox.__str__() == expected


def test_UnitBoxWindow_volume():
    unitBox = UnitBoxWindow(3)
    assert unitBox.volume() == 1
