import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    """BallWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a circle and in 3D a ball
    # ? and for dimension > 3
    """

    def __init__(self, centre, radius):
        """This method initializes the ball, thanks to the center of the ball and its radius.

        Args:
            centre (Liste): center of the ball  # ! list not List
            radius (int): radius of the ball
        """

        self.radius = radius
        self.centre = centre

    def __str__(self):
        """display the center and the radius of the ball
        # * with "display" one can expect a plot
        """
        # ! use a f-string
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

        Args:
            # ! point not args
            # ? array or list
            args (array): list of coordinates of the point
        """
        # * exploit numpy vectors, avoid loops
        dist = 0
        for i in range(len(point)):
            dist += (point[i] - self.centre[i]) ** 2
        dist = np.sqrt(dist)
        return dist <= self.radius

    def dimension(self):
        """Returns the number of dimension of the ball"""
        # ? what does "number of dimension" mean
        return len(self)

    def volume(self):
        """volume/area/length of the BallWindow

        Returns:
            int: volume/area/length
        """
        # ? why only for d <= 3, write a comment and mention it in docstring
        assert len(self) <= 3
        # * since each if contains a return, replace elif/else by simple if
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
        # Same remark as BoxWindow.indicator_function
        return self.__contains__(point)

    def rand_2d(self, n=1, seed=None):
        """generate n random numbers in a 2d ball window
        # ? random "numbers", no random points

        Args:
            n (int): number of points to generate
            seed (int): describe the generator. Defaults to None.
        """
        # ! rand_2d is not tested
        # ! self.rayon is not defined
        rng = get_random_number_generator(seed)
        L = []
        # * exploit numpy vectorization power to avoid looping
        for i in range(n):
            rayon = rng.uniform(0, self.rayon)
            teta = rng.uniform(0, 2 * np.pi)  # * theta or angle but not teta
            # ? are you sure (x, y) is uniformly distributed over the disk
            x = rayon * np.cos(teta) + self.center[0]
            y = rayon * np.sin(teta) + self.center[1]
            L.append([x, y])
        return L
