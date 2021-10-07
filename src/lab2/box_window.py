from lab2.utils import get_random_number_generator


# todo make a pass on the docstrings
# todo test all your methods
class BoxWindow:
    """[summary]"""

    def __init__(self, bounds):
        """initialization

        Args:
            bounds (list): return BoxWindow of the intervals of list
        """
        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: return BoxWindow: intervals
        """
        # ! use f-strings
        # * iterate over self.bounds
        dd = "BoxWindow: "  # ! naming: dd ?
        for i in range(len(self.bounds)):
            dd += "[" + str(self.bounds[i][0]) + ", " + str(self.bounds[i][1]) + "]"
            if i < len(self.bounds) - 1:
                dd += " x "
        return dd

    def __len__(self):
        """return number of points

        Returns:
            int: number of points
        """
        return 2 * len(self.bounds)

    def __contains__(self, point):
        """returns true if point contains in super box

        Args:
            point (list): list of point's coordinates

        Returns:
            bool: returns true if point contains in the box
        """
        # * exploit numpy vectorization power
        # * consider for (a, b), x in zip(self.bounds, point)
        for i in range(len(self.bounds)):
            if point[i] < self.bounds[i][0] or point[i] > self.bounds[i][1]:
                return False
        return True

    def dimension(self):
        """return the dimension of the box

        Returns:
            int: number of the intervals
        """
        return len(self.bounds)

    def volume(self):
        """calcul volume of the box

        Returns:
            float: the volume of the box
        """
        # * exploit numpy vectorization power
        p = 1
        for i in range(len(self.bounds)):
            p *= self.bounds[i][1] - self.bounds[i][0]
        return p

    def indicator_function(self, points):
        """list of true if the each point in points in the Box

        Args:
            args (list): list of bool
        """
        # * exploit numpy vectorization power
        # ? how would you handle multiple points
        l = []
        for x in points:
            l.append(x in self)
        return l

    # * consider merging this function into __contains__ and add if isinstance(xxx, BoxWindow)...
    def BoxBox(self, box):  # ! naming: snake_case
        """verify if box in box (same dimension)

        Args:
            box (BoxWindow): box

        Returns:
            bool: verify if box in box
        """

        for i in range(len(self.bounds)):
            if box[i][0] < self.bounds[i][0] or box[i][1] > self.bounds[i][1]:
                return False
        return True

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        points = []
        rng = get_random_number_generator(rng)
        # * convention: use _ for unused counters
        # * exploit numpy, rng.uniform(a, b, size=)
        # ! iterate over self.bounds
        for i in range(n):
            point = []
            for j in range(len(self.bounds)):
                point.append(
                    (
                        (self.bounds[j][1] - self.bounds[j][0]) * rng.random()
                        + self.bounds[j][0]
                    )[0]
                )
            points.append(point)
        return points

    def center(self):
        """return a the center of the box as list

        Returns:
            [list]: [center of box]
        """
        # * exploit numpy vectorization power
        # ? how about np.mean
        centre = []
        for x in self.bounds:
            centre.append((x[1] + x[0]) / 2)
        return centre


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """initialization

        Args:
            dimension (int): dimension of the box
            center (list, optional): the center of the box. Defaults to None.
        """
        # * exploit numpy vectorization power
        # ? how about np.add.outer
        bounds = [[center[i] - 0.5, center[i] + 0.5] for i in range(dimension)]
        super().__init__(bounds)
