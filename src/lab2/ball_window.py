import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    """Creates a window of circular shape"""

    def __init__(self, center, radius):
        """Initialize the ball window with the center point and the radius .

        Args:
            center (array): array of the center point
            radius (float): size of the radius of the ball window
        """
        self.center = center
        self.radius = radius

    def dimension(self):
        """Returns the dimension of the ball window

        Returns:
            integer : dimension of the ball window
        """
        return (self.center).shape[0]

    def volume(self):
        """Returns the volume created by the ball window

        Returns:
            integer : volume of the ball
        """
        if self.dimension() == 1:
            return 2 * self.radius
        elif self.dimension() == 2:
            return np.pi * self.radius ** 2
        elif self.dimension() == 3:
            return (4 / 3) * np.pi * self.radius ** 3
        else:
            raise Exception("dimension too high")

    def __contains__(self, point):
        """Indicates if the point is contained in the ball window.
        Returns True if the point is in the ball, returns False otherwise.

        Args:
            point (array): coordinates of the point that we want to know if it is part of the ball.
        """
        if point.shape == self.center.shape:
            N = np.linalg.norm(point - self.center)
            return np.all(N <= self.radius)
        else:
            raise Exception("incorrect size of the point")

    def indicator_function(self, point):
        """Indicator function of the ball window. Returns 1 if the point is in the ball, returns 0 otherwise.

        Args:
            point (array): coordinates of the point
        """
        return int(self.__contains__(point))

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BallWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)

        L = []
        for p in range(n):  # nb of points taken randomly in the box
            L.append(
                [
                    np.random.uniform(a - self.radius, a + self.radius)
                    for a in self.center
                ]
            )
        return np.array(L)
