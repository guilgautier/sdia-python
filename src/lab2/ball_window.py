import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    """Creates a window of circular shape"""

    # ? circular shape => ball shape
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
        # ? how about .size
        return self.center.shape[0]

    def volume(self):
        """Returns the volume created by the ball window

        Returns:
            integer : volume of the ball
        """
        # ! duplicate code, define a temporary variable = self.dimension()
        if self.dimension() == 1:
            return 2 * self.radius
        if self.dimension() == 2:
            return np.pi * self.radius ** 2
        if self.dimension() == 3:
            return (4 / 3) * np.pi * self.radius ** 3
        raise Exception("dimension too high")

    def __contains__(self, point):
        """Indicates if the point is contained in the ball window.
        Returns True if the point is in the ball, returns False otherwise.

        Args:
            point (array): coordinates of the point that we want to know if it is part of the ball.
        """
        # * isolate exception from body of the method
        if point.shape != self.center.shape:
            raise Exception("incorrect size of the point")

        N = np.linalg.norm(point - self.center)
        return np.all(N <= self.radius)

    def indicator_function(self, point):
        """Indicator function of the ball window. Returns 1 if the point is in the ball, returns 0 otherwise.

        Args:
            point (array): coordinates of the point
        """
        # todo same comments as in BoxWindow.indicator_function
        return int(self.__contains__(point))

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BallWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)

        # todo same comments as in BoxWindow.indicator_function
        L = []
        for p in range(n):  # nb of points taken randomly in the box
            L.append(
                [
                    np.random.uniform(a - self.radius, a + self.radius)
                    for a in self.center
                ]
            )
        return np.array(L)
