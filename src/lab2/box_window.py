import numpy as np

from lab2.utils import get_random_number_generator


# todo make a pass on the docstrings
#
class BoxWindow:
    """This class BoxWindow create a box with dimension [a1, b1] x ... x [an, bn]."""

    def __init__(self, bounds):
        """Create the attribute bounds of the class BoxWindow.

        Args:
            args (list): list of the dimensions (for example in dimension2 [a1, b1] x [a2, b2])
        """
        """On pourrait vérifier que bounds est de la forme nx2"""
        # ? why isn't the check implemented and tested
        self.bounds = np.array(bounds)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [str]: the points of the box in each dimensions. (BoxWindow: [a1, b1] x [a2, b2] x ... )
        """

        b = "BoxWindow: "
        # ! use f-strings
        # * consider for a, b in self.bounds
        for i in range(self.bounds.shape[0]):
            b += str(list(self.bounds[i])) + " x "
        return b[:-3]

    def shape(self):
        """This method enables to know the of the box.

        Returns:
            [str] : with the dimension of the box (n x 2)

        Le premier return permet d'avoir la première dimension.
        """
        # ? how about str(self.bounds.shape)
        return f"{self.bounds.shape[0]} x 2"

    def indicator_function(self, point):
        """Check if the point is contained in the BoxWindow

        Point:
            Point (list) : list with the coordinates of the point to be tested

        Returns:
            [bool] : True if the point is contained in the box, False if not.
        """
        # * consider for i, (a, b) in enumerate(self.bounds)
        a = True
        for i in range(self.bounds.shape[0]):
            if (self.bounds[i, 0] <= point[i]) and (point[i] <= self.bounds[i, 1]):
                a == True
            else:
                return False
        return a

    def dimension(self):
        """"""
        return {self.bounds.shape[0]}

    # ! wrong spelling of length
    # todo test it
    def lenght(self):
        """This method return the lenght for each dimension of the BoxWindow.

        Returns:
            [list] : l[i] with the lenght of the BoxWindow in dimension i

        """
        # * exploit numpy vectors, use np.diff
        l = []
        for i in range(self.bounds.shape[0]):
            l = l + [self.bounds[i][1] - self.bounds[i][0]]
        return l

    def volume(self):
        """It returns the volume of the BoxWindow, if dimension is greater (or equal) than 3, otherwise, it returns the area in dimension 2, the lenght in dimension 1.

        Returns:
            [str] : the volume of the BoxWindow.

        """
        x1 = self.bounds[:, 0]
        x2 = self.bounds[:, 1]
        # * exploit numpy vectors, use - or np.diff, and np.prod
        # ? why using abs, isn't x2 > x1, isn't it tested
        return np.prod(abs(x2 - x1))

    # todo test it
    def indicator_function_several(self, args):
        """Check if the several points are contained in the BoxWindow or not.

        Args:
            args (list): list of the points to be tested

        Returns:

            [list] : [list of booleans, with True if the point is contained in the BoxWindow, False if not]
        """
        # * Nice try to handle multiple points
        # ! however method contains is not defined
        a = []
        for i in range(len(args)):
            a = a + [self.contains(args[i])]

        return a

    # todo test it
    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        # * convention: use _ for unused counters
        # * exploit numpy, rng.uniform(a, b, size=n)
        points = []
        for i in range(n):
            point = []
            for (a, b) in self.bounds:
                point.append(rng.uniform(a, b))
            points.append(point)
        return points

    def center(self):
        """Returns the center of the BoxWindow

        Returns:
            [list]: [coordonnates of the center]
        """
        # * exploit numpy vectors
        # ? how about np.mean
        center = []
        for (a, b) in self.bounds:
            center.append((a + b) / 2)
        return center


# todo implement, document and test the class
class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(UnitBoxWindow, self).__init__()
