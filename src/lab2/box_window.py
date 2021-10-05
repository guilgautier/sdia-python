import numpy as np

from lab2.utils import get_random_number_generator


class BoxWindow:
    """Representation of a box defines by [a1,b1] x [a2,b2] x ..."""

    def __init__(self, bounds):
        """Constructor of a BoxWIndow

        Args:
            bounds (numpy.array): The bounds of the box.
                                It must be of dimension N * 2
        """
        # * use isinstance
        assert type(bounds) == np.ndarray
        # * use .shapes
        assert len(bounds.T) == 2
        # ? why converting, bounds is already np.array
        self.bounds = np.array(bounds)

    def __str__(self):
        """Returns for example the following string :
        "BoxWindow: [a_1, b_1] x [a_2, b_2]"

        Returns:
            # ! str not String
            String: The representation of the box
        """
        s = "BoxWindow: "
        # ! use f-strings
        if len(self.bounds) > 1:  # ? use self.dimension()
            # * consider for a, b in self.bounds[:-1]
            for k in range(0, len(self.bounds) - 1):
                # * use += opereator
                s = (
                    s
                    + "["
                    + str(self.bounds[k][0])
                    + ", "
                    + str(self.bounds[k][1])
                    + "]"
                    + " x "
                )
        s = (
            s
            + "["
            + str(self.bounds[len(self.bounds) - 1][0])
            + ", "
            + str(self.bounds[len(self.bounds) - 1][1])
            + "]"
        )
        return s

    def __len__(self):
        """Returns the len of the box, ie the dimension.

        Returns:
            int: the dimension of the box
        """
        return len(self.bounds)

    def __contains__(self, point):
        """Returns True if the point belongs to the box

        Args:
            point (numpy.array): the point

        Returns:
            Boolean: True if the point beyonds to the box
        """
        assert len(point) == len(self)  # ! readability: self.dimension()
        return all(a <= x <= b for (a, b), x in zip(self.bounds, point))

    def dimension(self):
        """Returns the dimension of the box, ie the number of segment.

        Returns:
            int: the dimension of the box
        """
        # ! readability: len(self)
        return self.__len__()

    def volume(self):
        """Returns the volume of the box, ie the multiplication of the size of each segment.

        Returns:
            int: the volume of the box
        """
        # * exploit numpy vectors, use - or np.diff, and np.prod
        V = 1  # ! naming: V => volume
        # * consider for a, b in self.bounds
        for k in range(0, len(self.bounds)):
            # ? why abs, isn't b > a, isn't it tested ?
            V *= np.abs(self.bounds[k][1] - self.bounds[k][0])
        return V

    def indicator_function(self, point):
        """Returns True if the point beyonds to the box

        Args:
            point (numpy.array): the point

        Returns:
            boolean: True if the point beyonds to the box
        """
        # ? how would you handle multiple points
        # ! readability: point in self
        return self.__contains__(point)

    def rand(self, n=1, rng=None):
        """Generate n points uniformly at random inside the BoxWindow.

        Args:
            n (int, optional): the number of points. Defaults to 1.
            rng (numpy.random._generator.Generator, optional): Random number generator. Defaults to None.

        Returns:
            A list of n points generated uniformly at random inside the BoxWindow.
        """
        rng = get_random_number_generator(rng)
        points = []
        for k in range(0, n):
            pointk = np.zeros(len(self.bounds))
            for i in range(0, len(self.bounds)):
                c = rng.uniform(self.bounds[i][0], self.bounds[i][1])
                pointk[i] = c
            points.append(pointk)
        return points


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center=None):
        """Returns a unit box window, with segments of length 1 for each dimension, centered on args if the center is precised, else, it is centered on (0,0,...,0).

        Args:
            dimension (int): The dimension of the box window
            center (numpy.array, optional): The array of the center of each segment of the box window. Defaults to None.
        """
        bounds = np.zeros(shape=(dimension, 2))
        # * avoid redundancy if/else cases should be put inside the for loop
        # * consider iterating over center if any
        if center == None:
            for k in range(0, dimension):
                bounds[k] = [-0.5, 0.5]
        else:
            # ? how do you make sure dimension matches with center
            for k in range(0, dimension):
                bounds[k] = [center[k] - 0.5, center[k] + 0.5]
        # * Nice use of super()
        super().__init__(bounds)
