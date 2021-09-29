import numpy as np
import pytest

from lab2.ball_window import BallWindow


def test_raises_exception_when_initializing_with_wrong_center():
    with pytest.raises(AssertionError):
        BallWindow(center=np.array([]), radius=5)


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0]), 5, 1),
        (np.array([0, 0]), 5, 2),
        (np.array([0, 0, 0]), 5, 3),
        (np.array([0, 0, 0, 0]), 5, 4),
    ],
)
def test_dimension(center, radius, expected):
    assert BallWindow(center, radius).dimension() == expected


def test_raises_exception_when_using_contains_with_invalid_dimension():
    with pytest.raises(AssertionError):
        ball = BallWindow(center=np.array([0, 0]), radius=5)
        x = np.array([1, 2, 3])
        x in ball


@pytest.fixture
def ball_2d():
    return BallWindow(center=np.array([0, 0]), radius=5)


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([0, 30]), False),
        (np.array([-6, 9]), False),
    ],
)
def test_indicator_function2D(ball_2d, point, expected):
    is_in = ball_2d.indicator_function(point)
    assert is_in == expected


@pytest.fixture
def ball_1d():
    return BallWindow(center=np.array([5]), radius=2)


@pytest.mark.parametrize(
    "point, expected", [(6, True), (4.5, True), (1, False),],
)
def test_indicator_function1D(ball_1d, point, expected):
    is_in = ball_1d.indicator_function(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "n, rng, expected",
    [(1, 0, np.array([[0.18864415955389333, 0.0799007050028547]])),],
)
def test_random_points_generation(n, rng, expected):
    box = BallWindow(center=np.array([0, 0]), radius=5)
    point = box.rand(n, rng)
    a = np.array_equal(point, expected)
    assert a


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0]), 2, 4),
        (np.array([0, 0]), 2, np.pi * 4),
        (np.array([0, 0, 0]), 2, np.pi * 2 ** 3 * 4 / 3),
    ],
)
def test_volume(center, radius, expected):
    assert BallWindow(center, radius).volume() == expected
