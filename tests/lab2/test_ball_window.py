import numpy as np
import pytest
from math import pi

from lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        ([2.5, 2.5], 1, "BallWindow: center[2.5, 2.5] & radius[1.0]."),
        ([0, 5], 14, "BallWindow: center[0, 5] & radius[14.0].")
    ],
)
def test_box_string_representation(center, radius, expected):
    assert BallWindow(center, radius).__str__() == expected


@pytest.fixture
def ball_2d_r3():
    return BallWindow(np.array([2.5, 2.5]), 1)

@pytest.mark.parametrize(
    "center, radius, expected",
    [
        ([2.5, 2.5], 1, 2),
        ([0, 5, 6], 14, 3)
    ],
)

def test_dim_ballWindow(center, radius, expected):
    assert len(BallWindow(center, radius)) == expected
 
@pytest.mark.parametrize(
    "point, expected",
    [
        ([2, 2.5], True),
        ([0, 5], False),
        ([3.5, 2.5], True)
    ],
)   
def test_contains_ball_2d_r3(ball_2d_r3,point, expected):
    assert (point in ball_2d_r3) == expected 
    
@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([[2, 2.5], [0, 10]]), np.array([1, 0])),
        (np.array([[0, 2.5], [2, 2]]), np.array([0, 1])),
        (np.array([3, 2.5]), True)
    ],
)   
def test_indicator_function_ball_2d_r3(ball_2d_r3,point, expected):
    assert np.all(ball_2d_r3.indicator_function(point) == expected)
    
def test_volume_ball_2d_3r(ball_2d_r3):
    assert round(ball_2d_r3.volume(), 10) == round(pi, 10) 
    
def test_random_ball_2d_3r(ball_2d_r3):
    assert np.all(ball_2d_r3.indicator_function(ball_2d_r3.rand(n=10)))