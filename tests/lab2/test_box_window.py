import numpy as np
import pytest

from lab2.box_window import BoxWindow, UnitBoxWindow, BallWindow


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


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), np.array([2.5])),
        (np.array([[0, 5], [0, 5]]), np.array([2.5, 2.5])),
        (
            np.array([[0, 5], [-1, 3], [-10, 10]]),
            np.array([2.5, 1, 0]),
        ),
    ],
)
def test_box_center(bounds, expected):
    assert (BoxWindow(bounds).center() == expected).all()


@pytest.mark.parametrize(
    "args, expected",
    [
        ((10, np.array([[2.5, 2.5]])), np.array([[2.5, 2.5]])),
    ],
)
def test_unit_box_center(args, expected):
    assert (UnitBoxWindow(*args).center() == expected).all()


@pytest.mark.parametrize(
    "args, expected",
    [
        ((np.array([[2.5, 2.5]]), 10), np.array([[2.5, 2.5]])),
    ],
)
def test_center_ball_window(args, expected):
    assert (BallWindow(*args).center == expected).all()


@pytest.mark.parametrize(
    "args,  expected",
    [
        ((np.array([[2.5, 2.5]]), 10, np.array([[2.5, 2.5]])), True),
        ((np.array([[2, 5]]), 4, np.array([[2.5, 2.5]])), True),
        ((np.array([[2, 2]]), .5, np.array([[2.5, 2.5]])), False),
        ((np.array([[0, 2, 3]]), .5, np.array([[1, 2.5, 2.5]])), False),
        ((np.array([[0, 2, 3, 4]]), 5, np.array([[1, 3, 2.5, 2.5]])), True),
    ],
)
def test_in_ball_window(args, expected):
    assert BallWindow(*args[:2]).__contains__(args[-1]) == expected
