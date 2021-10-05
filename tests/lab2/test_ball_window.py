import numpy as np
import pytest

from lab2.ball_window import BallWindow


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        (np.array([0]), 4, 4),
        (np.array([2.5, 2.5]), 3.7, 3.7),
        (np.array([-1, 5]), 2.0, 2.0),
        (np.array([10, 3]), 20000, 20000),
    ],
)
def test_radius(center, radius, expected):
    ball = BallWindow(center, radius)
    assert ball.radius == expected


@pytest.mark.parametrize(
    "box, expected",
    [
        (np.array([1]), 1),
        (np.array([1, 2.2]), 2),
        (np.array([1.4, 2.6, 3.9]), 3),
    ],
)
def test_dimension_box(box, expected):
    ball = BallWindow(box, 4)
    assert ball.dimension() == expected


# ? ball or center
# ! tests pass but on a wrong implementation
@pytest.mark.parametrize(
    "ball, radius, expected",
    [
        (np.array([1]), 2, 4),
        (np.array([1, 3]), 3, 36),
        (np.array([1.4, 2.6, 3.9]), 2.5, 125.0),
    ],
)
def test_volume_box(ball, radius, expected):
    ball = BallWindow(ball, radius)
    assert ball.volume() == expected


def test_contains_oneDimension():
    ball1 = BallWindow(np.array([1]), 3)
    ball2 = BallWindow(np.array([3.5]), 0.5)
    ball3 = BallWindow(np.array([-2.5]), 1.5)
    ball4 = BallWindow(np.array([0]), 2)
    assert ball1.__contains__(np.array([2]))
    assert not ball1.__contains__(np.array([5]))
    assert ball2.__contains__(np.array([4]))
    assert not ball2.__contains__(np.array([4.01]))
    assert ball3.__contains__(np.array([-3.9]))
    assert ball4.__contains__(np.array([0]))
    assert not ball4.__contains__(np.array([2.02]))


def test_contains_twoDimension():
    ball1 = BallWindow(np.array([0, 0]), 1)
    ball2 = BallWindow(np.array([3.5, 2.5]), 0.5)
    assert ball1.__contains__(np.array([0.5, 0.5]))
    assert not ball1.__contains__(np.array([1, 2]))
    assert ball2.__contains__(np.array([3.25, 2.75]))


def test_indicator_function_oneDimension():
    ball1 = BallWindow(np.array([1]), 3)
    ball2 = BallWindow(np.array([3.5]), 0.5)
    ball3 = BallWindow(np.array([-2.5]), 1.5)
    ball4 = BallWindow(np.array([0]), 2)
    assert ball1.indicator_function(np.array([2]))
    assert not ball1.indicator_function(np.array([5]))
    assert ball2.indicator_function(np.array([4]))
    assert not ball2.indicator_function(np.array([4.01]))
    assert ball3.indicator_function(np.array([-3.9]))
    assert ball4.indicator_function(np.array([0]))
    assert not ball4.indicator_function(np.array([2.02]))


def test_indicator_function_twoDimension():
    ball1 = BallWindow(np.array([0, 0]), 1)
    ball2 = BallWindow(np.array([3.5, 2.5]), 0.5)
    assert ball1.indicator_function(np.array([0.5, 0.5]))
    assert not ball1.indicator_function(np.array([1, 2]))
    assert ball2.indicator_function(np.array([3.25, 2.75]))


# ? does this raise a TypeError or an AssertionError
def test_raise_type_error_when_points_is_not_of_good_dimension():
    with pytest.raises(AssertionError):
        ball1 = BallWindow(np.array([0, 0]), 1)
        np.array([1, 2, 3]) in ball1


# def test_rand_onepoint_onedimension():
#    ball = BallWindow(np.array([1, 2]), 3)
#   assert ball.__contains__(ball.rand()[0])


def test_rand_multiplepoint_3dimension():
    ball = BallWindow(np.array([1, 15.5, 3.5]), 2)
    coord = ball.rand(100)
    for value in coord:
        assert ball.__contains__(value)
