from math import *  # ! never use wildcard imports, import the specific functions

import numpy as np

from lab2.utils import get_random_number_generator


# todo test the class
# todo write the docstrings
class BoxWindow:
    """[summary]"""

    def __init__(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        args = self.bounds
        hamza = ""  # ? why this variable name
        # * consider for i, (a, b) in enumerate(self.bounds)
        for i in range(0, len(args)):
            hamza = hamza + str(args[i])
            if i < len(args) - 1:
                hamza += " x "

        return "BoxWindow : " + hamza

    def __len__(self):
        args = self.bounds
        return len(args)

    def __contains__(self, args):
        Box_args = self.bounds  # ! Box_args not defined
        # * consider for (a, b), x in zip(self.bounds, point)
        for i in range(0, len(arg)):  # ! arg not defined
            a = args[i][0]
            b = args[i][1]
            c = box_args[i][0]  # ! box_args not defined
            d = box_args[i][1]
            if a < c or d < b:
                return False
        return True

    # todo describe you implementation of the docstring
    def dimension(self):
        """[summary]"""
        n = len(self.bounds)  # ? why not using self.dimension()
        return 2 * n

    def volume(self):
        """[summary]"""
        n = len(self.bounds)  # ? why not using self.dimension()
        args = self.bounds  # ? why this variable name
        V = 1  # ! V and v are different variables, your code may not work properly
        # * exploit numpy vectors, use - or np.diff, and np.prod
        for i in range(0, n):
            l = args[i][1] - args[i][0]
            v = v * l  # * use *= operator
        return v

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        Box_args = self.bounds
        n = len(Box_args)
        for i in range(0, n):
            a = Box_args[i][1]
            b = Box_args[i][0]
            if args[i] < b or arg[i] > a:  # ! arg not defined
                return False
        return True

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        n = len(self.bounds)
        args = self.bounds
        L = []
        # * exploit numpy, rng.uniform(a, b, size=n)
        for i in range(0, n):
            # ! random is not defined, please use rng
            a = random.uniform(args[i][0], args[i][1])
            L.append(a)
        L = np.array(L)
        return L

    def center(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        # * exploit numpy vectors, use - or np.diff, and +
        center = []
        n = len(self.bounds)
        for i in range(n):
            b_i = self.bounds[i][1]
            a_i = self.bounds[i][0]
            center.append((b_i + a_i) / 2)
        return center


# todo write the docstrings
class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        # ? how do you treat the case where center's dimension does not match dimension
        L = []  # ? why this variable name
        # * exploit numpy vectorization power
        for i in range(dimension):  # * consider for c in center
            L.append([center[i] - 0.5, center[i] + 0.5])
        super().__init__(L)  # * perfect use of super


class BallWindow:
    # todo test the class
    # todo write the docstrings
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def dimension(self):
        return len(self.center)

    def __contains__(self, point):
        s = 0
        # * consider for (a, b), x in zip(self.bounds, point)
        for i in range(dimension):  # ! dimension variable not defined
            s += (point[i] - self.center[i]) ** 2
        if s <= (self.radius) ** 2:
            return True
        return False

    def area(self):  # ? naming: how about surface
        n = len(self.center)  # ? why not using self.dimension()
        R = self.radius
        return 2 * (pi) ** (n / 2) * R ** (n - 1) / gamma(n / 2)

    def volume(self):
        n = len(self.center)  # ? why not using self.dimension()
        R = self.radius
        return (pi) ** (n / 2) * R ** (n) / gamma(n / 2 + 1)
