from lab2.utils import get_random_number_generator
import numpy as np


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
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        return "BoxWindow: " + " x ".join(l_str)

    def __len__(self):
        return len(self.bounds)

    def in_segment(self, x, segment):
        return segment[0] <= x < segment[1]

    def __contains__(self, x):

        return all(a <= x <= b for (a, b), x in zip(self.bounds, x))

    def dimension(self):
        """Returns number of dimensions of box window"""
        return len(self)

    def volume(self):
        """[summary]"""
        v = 1
        for dim in self.bounds:
            v *= np.abs(dim[0] - dim[1])
        return v

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return args in self

    def get_random_point_inside(self):
        return np.array([np.random.uniform(*dim) for dim in self.bounds])

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return [self.get_random_point_inside()] * n


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """

        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])

        super(self.__class__, self).__init__(bounds)
