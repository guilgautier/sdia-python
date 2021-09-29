from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """Represents a box in any dimension, defined by a number of segments."""

    def __init__(self, bounds):
        """Initializes the bounds with the np.array given as a parameter

        Args:
            bounds (np.array): array that contains the bound for each dimension
        """

        bounds = np.array(bounds)
        for segment in bounds:
            assert len(segment) == 2
        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            String: = string returned when doing print(BoxWindow(...))
        """

        string = ""
        for i, segment in enumerate(self.bounds):
            string += printSegment(segment)
            if i != (len(self.bounds) - 1):
                string += " x "
        result = "BoxWindow: " + string
        return result

    def __len__(self):
        """Returns the dimension of the box.

        Returns:
            int : The dimension of the box

        """
        return len(self.bounds)

    def __contains__(self, point):
        """Returns true if a point is in the box.

        Args:
            point (numpy.array): point to test

        Returns:
            Boolean: if the point is in the box
        """
        assert len(point) == len(self)

        for i, coord in enumerate(point):
            if not pointIsInSegment(coord, self.bounds[i]):
                return False
        return True
        # better implementation:
        # return all(a <= x <= b for(a, b), x in zip(self.bounds, point))

    def dimension(self):
        """Returns the dimension of the box.

        Returns:
            int : The dimension of the box
        """
        return len(self)

    def volume(self):
        """Returns the volume of the box.

        Returns:
            int: The volume of the box.
        """

        volume = 0 if len(self) == 0 else 1
        for segment in self.bounds:
            volume *= segmentLength(segment)

        return volume

    def indicator_function(self, point):
        """Returns true if a point is in the box.

        Args:
            point (numpy.array): point to test

        Returns:
            Boolean: if the point is in the box
        """
        return point in self

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        Returns:
            numpy.array: array containing all the generated points
        """
        rng = get_random_number_generator(rng)
        point_list = []
        for _ in range(n):
            point = []
            for segment in self.bounds:
                point.append(rng.uniform(segment[0], segment[1]))
            point_list.append(np.array(point))
        return np.array(point_list)


def printSegment(array):
    """Prints a segment using the format [float, float]

    Args:
        array (numpy.array): array representing the segment

    Returns:
        string: the segment printed in the correct format
    """
    return "[" + str(float(array[0])) + ", " + str(float(array[1])) + "]"


def segmentLength(segment):
    """Returns the length of a segment

    Args:
        segment (numpy.array): array representing the segment

    Returns:
        float: length of the segment
    """
    return segment[1] - segment[0]


def pointIsInSegment(point, segment):
    """Tells whether a point is contained in a segment

    Args:
        point (float): point to test
        segment (numpy.array): array representing the segment

    Returns:
        boolean: if the point is in the segment
    """
    return point <= segment[1] and point >= segment[0]


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
