import numpy as np
import pytest

from lab2.ball_window import BallWindow


@pytest.mark.parametrize(
    "box, expected",
    [(np.array([1]), 1), (np.array([1, 2.2]), 2), (np.array([1.4, 2.6, 3.9]), 3),],
)
def test_len_box(box, expected):
    assert len(BallWindow(box, 4)) == expected
