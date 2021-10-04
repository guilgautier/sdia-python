from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """Representation of a box defines by [a1,b1] x [a2,b2] x ...
    """

    def __init__(self, bounds):
        """Constructor of a BoxWIndow

        Args:
            bounds (numpy.array): The bounds of the box.
                                It must be of dimension N * 2
        """
        assert type(bounds) == np.ndarray
        assert len(bounds.T) == 2
        self.bounds = np.array(bounds)

    def __repr__(self):
        """Return for example the following string :
        "BoxWindow: [a_1, b_1] * [a_2, b_2]"

        Returns:
            String: The representation of the box
        """
        s = "BoxWindow: "
        if len(self.bounds) == 1:
            s = s + "[" + str(self.bounds[0][0]) + ", " + str(self.bounds[0][1]) + "]"
            return s
        else:
            for k in range(0, len(self.bounds) - 1):
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
        """Return the len of the box, ie the dimension.

        Returns:
            int: the dimension of the box
        """
        return len(self.bounds)

    def __contains__(self, point):
        """Return True if the point beyonds to the box

        Args:
            point (numpy.array): the point

        Returns:
            Boolean: True if the point beyonds to the box
        """
        assert len(point) == len(self)
        return all(a <= x <= b for (a, b), x in zip(self.bounds, point))

    def dimension(self):
        """[summary]
        """
        return self.__len__()

    def volume(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        V = 1
        for k in range(0, len(self.bounds)):
            V *= np.abs(self.bounds[k][1] - self.bounds[k][0])
        return V

    def indicator_function(self, point):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return self.__contains__(point)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        points = np.zeros((n, len(self.bounds)))
        for k in range(0, n):
            for i in range(0, len(self.bounds)):
                c = rng.uniform(self.bounds[i][0], self.bounds[i][1])
                points[k][i] = c
        return points


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
