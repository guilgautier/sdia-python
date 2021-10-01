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
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0.0, 5.0] x [0.0, 5.0]"),
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
        (np.array([[2.5, 2.5]]), 1),
        (np.array([[0, 5], [0, 5]]), 2),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            3,
        ),
    ],
)
def test_box_len(bounds, expected):
    assert len(BoxWindow(bounds)) == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 1),
        (np.array([[0, 5], [0, 5]]), 2),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            3,
        ),
    ],
)
def test_box_dimension(bounds, expected):
    assert BoxWindow(bounds).dimension() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([]), 0),
        (np.array([[3, 6]]), 3),
        (np.array([[0, 5], [0, 5]]), 25),
        (np.array([[0, 5], [0.5, 1.5], [2, 3]]), 5),
    ],
)
def test_box_volume(bounds, expected):
    assert BoxWindow(bounds).volume() == expected


def test_raises_exception_when_point_of_wrong_dimension():
    # ! raise an exception in BoxWindow.__contains__() instead of assert
    with pytest.raises(AssertionError):
        np.array([0, 0, 3]) in BoxWindow(np.array([[0, 5], [0, 5]]))


def test_raises_exception_when_initializing_with_wrong_array():
    # ! raise an exception in BoxWindow.__init__() instead of assert
    with pytest.raises(AssertionError):
        BoxWindow(np.array([[0, 5, 2], [0, 5]]))


@pytest.mark.parametrize(
    "n, rng, expected",
    [
        (1, 0, np.array([[3.1848084366072715, 1.3489335688193516]])),
    ],
)
def test_random_points_generation(n, rng, expected):
    # ? rather test that the output has correct number of points and dimension
    box = BoxWindow(np.array([[0, 5], [0, 5]]))
    point = box.rand(n, rng)
    a = np.array_equal(point, expected)
    # * consider using np.testing.assert_array_equal without assert
    assert a
