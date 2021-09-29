from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, boundsArg):
        """Initialize the BoxWindows from the bounds given in the array.

        Args:
            args (array): array of bounds containing the coordinates of each bound
        """
        self.bounds = np.array(boundsArg)

    def __str__(self):
        """Display the BoxWindow in a string

        Returns:
            [string]: BoxWindows points coordinates
        """
        description = "BoxWindow: "
        for i in range(len(self.bounds)):
            description = description + str(list(self.bounds[i])) + " x "
        return description[:-3]

    def __len__(self):
        return self.bounds.size

    def __contains__(self, point):
        # assert len(point) == len(self)  ##Test if the point has the same dimension
        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        return np.all(np.logical_and(a <= point, point <= b))

    def dimension(self):
        """[summary]"""
        return len(self)

    def volume(self):
        """[summary]"""
        dim = len(self)
        volume = 1
        for i in range(0, dim - 1):
            long = abs(self.bounds[i][0] - self.bounds[i][1])
            volume = volume * long
        return volume

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        # super(BoxWindow, self).__init__(args)
