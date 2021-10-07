import numpy as np

from lab2.utils import get_random_number_generator


# todo test your exceptions
class BoxWindow:
    """Creates a window of rectangular shape"""

    def __init__(self, args):
        """Initialize the box window with the bounding points.

        Args:
            args (array): array of the bounding points of the box, must be of dimension (d,2). Each segment of the form [a,b] with a<=b.
        """
        if np.all(np.diff(args) >= 0):  # checks if a<=b for each segment
            self.bounds = args
        else:
            # ! raise a more concrete exception https://docs.python.org/3/library/exceptions.html#concrete-exceptions
            raise Exception("incorrect bounds")

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str : give the bounds of the box
        """

        def remove_zero(w):
            int_w = int(w)
            return int_w if int_w == w else w

        mot = ""
        # ! use f-strings
        for a, b in self.bounds:
            mot = mot + str([remove_zero(a), remove_zero(b)]) + " x "
        return "BoxWindow: " + mot[:-3]  # mot[:-3] to remove the last " x "

    def length(self):
        """Returns an array of the length of each segment (one for each direction)

        Returns:
            array : array of the length in each direction
        """
        a, b = self.bounds[:, 0], self.bounds[:, 1]
        # ? how about np.diff
        return b - a

    def __len__(self):
        """Returns the len of the box window

        Returns:
            float : sum of the length of each segment (direction)
        """
        length = self.length()
        return sum(length)

    def __contains__(self, point):
        """Indicates if the point is contained in the box window.
        Returns True if the point is in the box, returns False otherwise.

        Args:
            point (array): coordinates of the point that we want to know if it is part of the box.
        """
        # ? use .ndim and .size
        if point.shape == (self.dimension(),):
            a, b = self.bounds[:, 0], self.bounds[:, 1]
            return np.all(a <= point) and np.all(point <= b)
        else:
            # ! raise a more concrete exception https://docs.python.org/3/library/exceptions.html#concrete-exceptions
            raise Exception("incorrect size of the point")

    def dimension(self):
        """Returns the dimension of the box window

        Returns:
            integer : dimension of the box
        """
        return len(self.bounds)

    def volume(self):
        """Returns the volume created by the box window

        Returns:
            integer : volume of the box
        """
        return np.prod(self.length())

    def indicator_function(self, point):
        """Indicator function of the box window. Returns 1 if the point is in the box, returns 0 otherwise.

        Args:
            point (array): coordinates of the point
        """
        # ? how would you handle multiple points
        # ! use "point in self"
        return int(self.__contains__(point))

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)

        L = []
        # * convention: use _ for unused counters
        # * exploit numpy, rng.uniform(a, b, size=)
        for p in range(n):  # nb of points taken randomly in the box
            # ! use rng
            L.append([np.random.uniform(a, b) for (a, b) in self.bounds])
        return np.array(L)


# heritage
class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """Initialize unitary box window given an array for the center point(s) and dimension

        Args:
            dimension ([integer]): dimension of the box window
            center (np.array()): Each element of the array is the center of one segment of the box. The array is of the shape (dimension,). Defaults to None.
        """
        if (dimension,) != center.shape:
            raise Exception("incorrect dimension or incorrect center")
        else:
            self.center = center
            self.dimension = dimension

            bounds = []
            for k in center:
                bounds.append([k - 0.5, k + 0.5])
            bounds = np.array(bounds)

            super(UnitBoxWindow, self).__init__(bounds)
