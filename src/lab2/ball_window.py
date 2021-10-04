import numpy as np


class BallWindow:
    def __init__(self, center, radius):

        self.center = np.array(center)
        self.radius = radius

    def __contains__(self, point):
        """This function checks if a points is in the ball or not
        Args:
            point ([type]): [description]
        """
        all(abs(i - j) < self.radius for i, j in point, self.center)
