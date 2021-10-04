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
@pytest.mark.parametrize(
    "point, expected",
    [(np.array([1, 1]), True), (np.array([0, 5]), True), (np.array([1, 7]), False)],
)
def test_box2d_contains(box_2d_05, point, expected):
    contain = point in box_2d_05
    assert contain == expected


@pytest.mark.parametrize(
    "BoxWindow, expected",
    [(BoxWindow([[1, 3], [2, 6]]), 8), (BoxWindow([[1, 8], [2, 4]]), 14)],
)
def test_volume(BoxWindow, expected):
    vol = BoxWindow.volume()
    assert vol == expected
    
@pytest.fixture
def box_3d_05():
    return BoxWindow(np.array([[0, 5], [0, 5], [0, 5]]))

@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0, 0]), True),
        (np.array([2.5, 2.5, 2.5]), True),
        (np.array([-1, 5, 5]), False),
        (np.array([0, 3, 7]), False),
    ],
)
def test_indicator_function_box_3d(box_3d_05, point, expected):
    is_in = box_3d_05.indicator_function(point)
    assert is_in == expected

@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([[0, 0, 0], [1, 2, 4]]), np.array([1, 1])),
        (np.array([[2.5, 2.5, 2.5], [2, 2, 2]]), np.array([1, 1])),
        (np.array([[-1, 5, 5], [2, 3, 5]]), np.array([0, 1])),
        (np.array([[0, 3, 7], [0, 5, 10]]), np.array([0, 0])),
    ],
)
def test_indicator_function_multiple_box_3d(box_3d_05, point, expected):
    is_in = box_3d_05.indicator_function(point)
    assert np.all(is_in == expected)
    

def test_random_generator_box_3d(box_3d_05):
    assert np.all(box_3d_05.indicator_function(box_3d_05.rand(n=10)))