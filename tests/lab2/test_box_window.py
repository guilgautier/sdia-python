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
            "BoxWindow: [0, 5] x [-1.45, 3.14] x [-10, 10]",
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


# checks if the dimension of the window box is correct (d,2).
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), (3, 2)),
        (np.array([[2.5, 2.5]]), (1, 2)),
    ],
)
def test_init(bounds, expected):
    c = BoxWindow(bounds)
    assert c.bounds.shape == expected


# checks the evaluation of the length of each bound is correct.
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), np.array([5, 5])),
        (np.array([[2.5, 2.5]]), np.array([0])),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), np.array([5.0, 4.59, 20.0])),
    ],
)
def test_length(bounds, expected):
    c = BoxWindow(bounds)
    assert np.all(c.length() == expected)


# checks if the len of the box window is correct.
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 10),
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 29.59),
    ],
)
def test_len(bounds, expected):
    c = BoxWindow(bounds)
    assert c.__len__() == expected


# checks if for the box_2d, the points are in the box window
@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains(box_2d_05, point, expected):
    is_in = box_2d_05.__contains__(point)
    assert is_in == expected


# checks if the dimension of the box window is correct
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 2),
        (np.array([[2.5, 2.5]]), 1),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 3),
    ],
)
def test_dimension(bounds, expected):
    c = BoxWindow(bounds)
    assert c.dimension() == expected


# checks if the evaluation of the volume of the box is correct
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 25),
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), 459),
    ],
)
def test_volume(bounds, expected):
    c = BoxWindow(bounds)
    assert c.volume() == expected


# checks if the indicator function returns 1 if the point is in the box, 0 otherwise
@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1]), 1),
        (np.array([2.5, 2.5]), 1),
        (np.array([-1, 5]), 0),
        (np.array([10, 3]), 0),
    ],
)
def test_indicator_function(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


# checks if the point taken randomly is in the box
@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), True),
        (np.array([[2.5, 2.5]]), True),
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), True),
    ],
)
def test_rand(bounds, expected):
    c = BoxWindow(bounds)
    assert c.__contains__(c.rand(1)[0]) == expected


# checks if the box window created is unitary (the length of each segment = 1)
@pytest.mark.parametrize(
    "center, dimension, expected",
    [
        (np.array([2, 3]), 2, [1.0, 1.0]),
        (np.array([1, 1, 1]), 3, [1.0, 1.0, 1.0]),
        (np.array([0]), 1, [1.0]),
    ],
)
def test_UnitBoxWindow_init(center, dimension, expected):
    d = UnitBoxWindow(center, dimension)
    assert np.all(d.length() == expected)
