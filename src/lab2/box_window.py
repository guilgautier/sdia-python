from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""
    def __init__(self, args):
        """Create bow window

        Args:
            args (list of N float array): [a, b] bounds for each of the N dimensions of the window box.
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: string representation of the box window.
        """
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        return "BoxWindow: " + " x ".join(l_str)

    def __len__(self):
        return len(self.bounds)

    def in_segment(self, x, segment):
        """Tool function indicating if a point is in a given segment or not.

        Args:
            x (float array): point of interest
            segment (float array): segment considered

        Returns:
            bool: True if point is in the segment else False
        """
        return segment[0] <= x < segment[1]

    def __contains__(self, x):

        return all(a <= x <= b for (a, b), x in zip(self.bounds, x))

    def dimension(self):
        """Returns the number of dimension of the window box

        Returns:
            int: number of dimensions.
        """
        return len(self)

    def volume(self):
        """Returns the volume of the window box defined as the product of size of each dimension.

        Returns:
            float: volume of the window box.
        """
        v = 1
        for dim in self.bounds:
            v *= np.abs(dim[0] - dim[1])
        return v

    def indicator_function(self, args):
        """Returns if args is in the window box.

        Args:
            args (float array): The window box [description]

        Returns:
            [type]: [description]
        """
        return args in self

    def get_random_point_inside(self):
        """Returns a point at random in the window box

        Returns:
            float array: random point in the bow window
        """

        return np.array([np.random.uniform(*dim) for dim in self.bounds])

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return [self.get_random_point_inside()] * n

    def center(self):
        """Compute center of the box window.

        Returns:
            float array: center coordinates of the box window.
        """
        mid = lambda x: (x[0] + x[1]) / 2
        c = list(map(mid, self.bounds))
        return np.array(c)


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center):
        """[summary]

        Args:
            dimension (float): [description]
            center (float array, optional): center of the window.
        """

        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])

        super(UnitBoxWindow, self).__init__(bounds)
