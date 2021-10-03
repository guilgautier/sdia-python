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


def test_init():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.bounds.shape == (3, 2)


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [-1.45, 3.14], [-10, 10]]), (3, 2)),
        (np.array([[2.5, 2.5]]), (1, 2)),
    ],
)
def test_init2(bounds, expected):
    c = BoxWindow(bounds)
    assert c.bounds.shape == expected


def test_len():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.__len__() == [5.0, 4.59, 20.0]


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), [5, 5]),
        (np.array([[2.5, 2.5]]), [0]),
    ],
)
def test_len2(bounds, expected):
    c = BoxWindow(bounds)
    assert c.__len__() == expected


def test_contains():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    point1 = np.array([1, 0, 0])
    assert (c.__contains__(point1)) == True


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
def test_contains2(box_2d_05, point, expected):
    is_in = box_2d_05.__contains__(point)
    assert is_in == expected


def test_dimension():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.dimension() == 3


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 2),
        (np.array([[2.5, 2.5]]), 1),
    ],
)
def test_dimension2(bounds, expected):
    c = BoxWindow(bounds)
    assert c.dimension() == expected


def test_volume():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert (c.volume()) == 459


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), 25),
        (np.array([[2.5, 2.5]]), 0),
    ],
)
def test_volume2(bounds, expected):
    c = BoxWindow(bounds)
    assert c.volume() == expected






def test_indicator_function():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    point1 = np.array([1, 0, 0])
    assert (c.indicator_function(point1)) == 1


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
def test_indicator_function2(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected




def test_rand():
    c = BoxWindow(np.array([[0, 5], [-1.45, 3.14], [-10, 10]]))
    assert c.__contains__(c.rand(1)[0]) == True


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[0, 5], [0, 5]]), True),
        (np.array([[2.5, 2.5]]), True),
    ],
)
def test_rand2(bounds, expected):
    c = BoxWindow(bounds)
    assert c.__contains__(c.rand(1)[0]) == expected


def test_UnitBoxWindow_init():
    d=UnitBoxWindow(np.array([2,3]),2)
    assert d.__len__() == [1.0,1.0]
