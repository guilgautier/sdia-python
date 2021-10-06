import numpy as np
import pytest

from lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


# checks if the dimension of the ball window is correct
@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([0, 5]), 2),
        (np.array([2.5]), 1),
        (np.array([0, 5, 6]), 3),
    ],
)
def test_dimension(center, expected):
    c = BallWindow(center, 6)
    assert c.dimension() == expected


# checks if the volume of the ball window is correct
@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0, 5]), 2, np.pi * 4),
        (np.array([2.5]), 3, 6),
        (np.array([0, 5, 6]), 2, (4 / 3) * np.pi * 2 ** 3),
    ],
)
def test_volume(center, radius, expected):
    c = BallWindow(center, radius)
    assert c.volume() == expected


# checks if, for the ball_2d, the point is in the ball window
@pytest.fixture
def ball_2d():
    return BallWindow(np.array([0, 0]), 5)


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([10, 3]), False),
    ],
)
def test_contains_ball_2d(ball_2d, point, expected):
    is_in = ball_2d.__contains__(point)
    assert is_in == expected


# checks if for the ball_2d, the point is in the ball window. Returns 1 if it is the case, 0 otherwise.
@pytest.fixture
def ball_2d():
    return BallWindow(np.array([0, 0]), 5)


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), 1),
        (np.array([2.5, 2.5]), 1),
        (np.array([10, 3]), 0),
    ],
)
def test_indicator_ball_2d(ball_2d, point, expected):
    is_in = ball_2d.__contains__(point)
    assert is_in == expected


# checks if the point(s) taken randomly is in the ball window
@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0, 0]), 5, True),
        (np.array([1]), 3, True),
        (np.array([0, 0, 3]), 1, True),
    ],
)
def test_rand(center, radius, expected):
    c = BallWindow(center, radius)
    assert c.__contains__(c.rand(1)[0]) == expected
