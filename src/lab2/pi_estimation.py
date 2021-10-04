from src.lab2.box_window import BallWindow, BoxWindow, UnitBoxWindow
import numpy as np


def calcul_pi(n):
    """compute a simple estimation of pi with the Monte Carlo method
    generates a square and a quadrant inscribed within it
    random points are generated uniformly inside the square
    the proportion of point which are in the circle is an estimation of pi/4

    Args:
        n (int): numbers of random points to be generated

    Returns:
        [float]: estimation of pi
    """
    unitBox = UnitBoxWindow(np.array([0.5, 0.5]))
    unitBall = BallWindow(np.array([0, 0]), 1)
    pointsAlea = unitBox.rand(n)
    piEstim = 0
    for point in pointsAlea:
        if point in unitBall:
            piEstim += 1
    return 4 * piEstim / n
