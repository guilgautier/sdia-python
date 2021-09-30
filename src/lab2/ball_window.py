from lab2.utils import get_random_number_generator
import numpy as np


class BallWindow:
    """BallWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a circle and in 3D a ball"""

    def __init__(self, centre, radius):
        """This method initializes the ball, thanks to the center of the ball and its radius.

        Args:
            centre (Liste): center of the ball
            radius (int): radius of the ball
            """

        self.radius = radius
        self.centre = centre

    def __str__(self):
        """display the center and the radius of the ball
        """

        return (
            "BallWindow with centre: "
            + str(self.centre)
            + " and radius: "
            + str(self.radius)
        )

    def __len__(self):
        """Returns the number of dimension of the ball"""
        return len(self.centre)

    def __contains__(self, point):
        """Returns true if a point is contained in the ball. The coordinates of the point are given in parameter.

        args:
            args (array): list of coordinates of the point
        """
        dist = 0
        for i in range(len(point)):
            dist += (point[i] - self.centre[i]) ** 2
        dist = np.sqrt(dist)
        return dist <= self.radius

    def dimension(self):
        """Returns the number of dimension of the ball"""
        return len(self)

    def volume(self):
        """volume/area/length of the BallWindow

        Returns:
            int: volume/area/length
        """
        assert len(self) <= 3
        if len(self) == 3:
            return (4 * np.pi * self.radius ** 3) / 3
        elif len(self) == 2:
            return np.pi * self.radius ** 2
        else:
            return 2 * self.radius

    def indicator_function(self, point):
        """return the image of the point through the indicator function described by the ball window

        Args:
            args (array): points to test
        """
        return self.__contains__(point)

    def rand_2d(self, n=1, seed=None):
        """generate n random numbers in a 2d ball window

        Args:
            n (int): number of points to generate
            seed (int): describe the generator. Defaults to None.
        """
        rng = get_random_number_generator(seed)
        L = []
        for i in range(n):
            rayon = rng.uniform(0, self.rayon)
            teta = rng.uniform(0, 2 * np.pi)
            x = rayon * np.cos(teta) + self.center[0]
            y = rayon * np.sin(teta) + self.center[1]
            L.append([x, y])
        return L
