from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """Representation of [a1,b1] x [a2,b2] x ...
    """

    def __init__(self, bounds):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = np.array(bounds)

    def __repr__(self):
        """BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        s = "BoxWindow: "
        if len(self.bounds) == 1:
            s = s + "[" + str(self.bounds[0]) + "]"
            return s
        else:
            for k in range(0, len(self.bounds) - 1):
                s = s + "[" + str(self.bounds[k]) + "]" + " x "
            s = s + "[" + str(self.bounds[len(self.bounds) - 1]) + "]"
            return s

    def __len__(self):
        return len(self.bounds)

    def __contains__(self, point):
        assert len(point) == len(self)
        return all(a <= x <= b for (a, b), x in zip(self.bounds, point))

    def dimension(self):
        """[summary]
        """
        return self.__len__()

    def volume(self):
        """[summary]
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
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
