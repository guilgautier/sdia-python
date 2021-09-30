import numpy as np
import pytest

from lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.fixture
def ball_2d():
    return BallWindow(np.array([5, 5]), 5)


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([5, 5]), True),
        (np.array([0, 5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(ball_2d, point, expected):
    is_in = ball_2d.indicator_function(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([5, 5]), True),
        (np.array([0, 5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains(ball_2d, point, expected):
    is_in = point in ball_2d
    assert is_in == expected


@pytest.mark.parametrize(
    "center, rayon, expected", [(np.array([0, 0]), 1, np.pi),],
)
def test_volume(center, rayon, expected):
    assert BallWindow(center, rayon).volume() == expected
