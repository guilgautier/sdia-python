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
        """BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """

        shape = (self.bounds).shape
        representation = "BoxWindow: "
        for i in range(shape[0] - 1):
            representation = representation + str((self.bounds)[i]) + " x "

        representation = representation + str((self.bounds)[shape[0] - 1])
        return representation

    def __len__(self):
        return ((self.bounds).shape)[0]

    def __contains__(self, args):
        flag = True
        for i in self.__len__():
            if args[i] >= self.bounds[i][0] and args[i] <= self.bounds[i][0]:
                flag = True
            else:
                return False

        return flag

    def dimension(self):
        """[summary]"""
        return self.__len__()

    def volume(self):
        """[summary]"""
        v = 1
        for i in range(self.dimension()):
            v = v * abs((self.bounds[i][1] - self.bounds[i][0]))

        return v

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        if self.__contains__(args):
            return 1
        else:
            return 0

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


# a finir
bounds = np.array([[1, 2], [2, 3]])

box = BoxWindow(bounds)

print(box.__str__())
