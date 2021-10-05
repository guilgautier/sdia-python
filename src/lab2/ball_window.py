import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    """This class represents a ball according to the norm 1 of any dimension"""

    def __init__(self, center, radius):
        """Constructor of the class : build a ball whose dimension is given by the size of the center array and the radius by the float radius.

        Args:
            center (numpy.array): an array containing the coordinates of the center.
            radius (float): the radius of the ball.
        """
        self.center = center
        self.radius = radius

    # ? what is this method used for
    # ! __radius__ is not a conventional magic method
    # ! radius is already an attribute -> self.radius
    def __radius__(self):
        """Returns the radius of the ball.

        Returns:
            float: the radius of the ball
        """
        return self.radius

    def __contains__(self, point):
        """Return True if the ball contains the point given in argument.

        Args:
            point (numpy.array): a point represented by a numpy array of same size that the center.

        Returns:
            boolean: True if the ball contains the point given in argument
        """
        assert len(point) == len(self.center)
        # * exploit numpy vectorization power
        # ? how about np.linalg.norm
        for k in range(0, len(point)):
            if not (
                self.center[k] - self.radius <= point[k] <= self.center[k] + self.radius
            ):
                return False
        return True

    def dimension(self):
        """Returns the dimension of the ball.

        Returns:
            int: the dimension of the ball
        """
        return len(self.center)

    def volume(self):
        """Returns the volume of the box

        Returns:
            float: Returns the volume of the box
        """
        # todo rewrite the method
        # ! the volume (area) of a disk = pi r^2
        # ? is this tested
        return (2 * self.radius) ** self.dimension()

    def indicator_function(self, point):
        """Return True if the ball contains the point given in argument.

        Args:
            point (numpy.array): a point represented by a numpy array of same size that the center.

        Returns:
            boolean: True if the ball contains the point given in argument
        """
        # ? how would you handle multiple points
        return self.__contains__(point)

    def rand(self, numberOfPoints=1, rng=None):
        """Generate n points uniformly at random inside the BallWindow.

        Args:
            numberOfPoints (int, optional): Number of points. Defaults to 1.
            rng ((numpy.random._generator.Generator, optional): Random number generator. Defaults to None.

        Returns:
            list: A list of n points generated uniformly at random inside the BallWindow.
        """
        rng = get_random_number_generator(rng)
        points = []
        # ! naming: snake case for variables number_of_points
        # ! readability
        # * exploit numpy, rng.uniform(a, b, size=n)
        for k in range(0, numberOfPoints):
            pointk = np.zeros([self.dimension()])
            # * iterate over self.center
            for i in range(0, self.dimension()):
                c = rng.uniform(
                    self.center[i] - self.radius,
                    self.center[i] + self.radius,
                )
                pointk[i] = c
            points.append(pointk)
        return points
        # ? are you sure points are uniformly distributed
