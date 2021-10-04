import numpy as np
from lab2.utils import get_random_number_generator


class BallWindow:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __radius__(self):
        return self.radius

    def __contains__(self, point):
        # assert len(point) == len(self.center)
        for k in range(0, len(point)):
            if not (
                self.center[k] - self.radius <= point[k] <= self.center[k] + self.radius
            ):
                return False
        return True

    def dimension(self):
        return len(self.center)

    def volume(self):
        return (2 * self.radius) ** self.dimension()

    def indicator_function(self, point):
        return self.__contains__(point)

    def rand(self, numberOfPoints=1, rng=None):
        rng = get_random_number_generator(rng)
        points = []
        for k in range(0, numberOfPoints):
            pointk = np.zeros([self.dimension()])
            for i in range(0, self.dimension()):
                c = rng.uniform(
                    self.center[i] - self.radius, self.center[i] + self.radius,
                )
                pointk[i] = c
            points.append(pointk)
        return points
