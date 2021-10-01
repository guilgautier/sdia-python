import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    def __init__(self, center, radius):
        """Represents a ball in any dimension, defined by a center and a radius

        Args:
            center (numpy.array): coordinates of the center point
            radius (float): float representing the radius
        """
        center = np.array(center)
        # * simplys use assert len(center) or raise exception
        assert len(center) >= 1

        self.center = center
        # ? why taking abs(), radius must be positive
        self.radius = float(abs(radius))

    def __str__(self):
        # ! not implemented
        pass

    def __len__(self):
        """Returns the dimension of the ball

        Returns:
            int : dimension of the ball
        """
        return len(self.center)

    def __contains__(self, point):
        """Tells whether a point is contained in the ball

        Args:
            point (numpy.array): the point to test

        Returns:
            boolean: if it is contained in the ball
        """
        point = np.array(point)
        assert self.dimension() == point.size

        # * exploit numpy vectorize point - self.center
        difference = np.subtract(point, self.center)
        return np.linalg.norm(difference) <= self.radius

    def dimension(self):
        """Returns the dimension of the ball

        Returns:
            int : dimension of the ball
        """
        return len(self)

    def volume(self):
        """Returns the volume of the ball. The formula for the volume of an n-ball is used : https://fr.wikipedia.org/wiki/N-sph%C3%A8re

        Returns:
            float : volume of the ball
        """
        # * nice, consider using scipy.special
        n = self.dimension()
        R = self.radius
        if n % 2 == 0:  # formula in case dimension is even
            return (((np.pi) ** (n / 2)) * R ** n) / np.math.factorial(n / 2)
        else:  # formula in case dimension is odd
            odds = [i for i in range(1, n + 1, 2)]
            product = np.product(odds)
            return 2 ** ((n + 1) / 2) * np.pi ** ((n - 1) / 2) * R ** n / product

    def indicator_function(self, point):
        # todo handle multiple points
        return point in self

    def rand(self, n=1, rng=None):
        """Generates n points in the ball.

        Args:
            n (int, optional): Number of points generated. Defaults to 1.
            rng (int, optional): Random seed. Defaults to None.

        Returns:
            numpy.array: array containing the n generated points
        """
        rng = get_random_number_generator(rng)
        point_list = []

        # * exploit numpy vectorization power to avoid looping
        # ? are you sure vector is indeed uniformly distributed
        for _ in range(n):
            # a random direction is chosen from a random vector
            direction = rng.random(self.dimension())
            # a random distance from the center is chosen
            distance = rng.uniform(0, self.radius)
            # a vector of norm inferior to the radius is found by normalizing the random vector, and multiplying it by the random distance
            vector = np.multiply(direction, distance / np.linalg.norm(direction))
            # the chosen point is obtained by adding the center to the vector
            point_list.append(np.add(vector, self.center))

        return np.array(point_list)
