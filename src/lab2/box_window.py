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
            representation = (
                representation
                + "["
                + str((self.bounds)[i][0])
                + ", "
                + str((self.bounds)[i][1])
                + "]"
                + " x "
            )

            # representation = (
            #     representation
            #     + np.array2string(
            #         (self.bounds)[i], precision=2, separator=", ", suppress_small=True
            #     )
            #     + " x "
            # )

        representation = (
            representation
            + "["
            + str((self.bounds)[shape[0] - 1][0])
            + ", "
            + str((self.bounds)[shape[0] - 1][1])
            + "]"
        )
        # representation = representation + np.array2string(
        #     (self.bounds)[shape[0] - 1],
        #     precision=2,
        #     separator=", ",
        #     suppress_small=True,
        # )
        return representation

    def __len__(self):
        return ((self.bounds).shape)[0]

    def __contains__(self, args):
        flag = True
        for i in range(self.__len__()):
            if args[i] >= self.bounds[i][0] and args[i] <= self.bounds[i][1]:
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
            return True
        else:
            return False

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        L = np.ones((n, self.__len__()))  # liste des points
        for i in range(n):
            if self.__len__() == 1:
                L[i] = (1 - rng.random()) * self.bounds[0] + rng.random() * self.bounds[
                    1
                ]

            elif self.__len__() != 1:
                for j in range(self.__len__()):

                    L[i][j] = (1 - rng.random()) * self.bounds[j][
                        0
                    ] + rng.random() * self.bounds[j][1]

        return L


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)


bounds = np.array([[0.5, 0.7], [0.5, 0.7]])
box = BoxWindow(bounds)

print(box.rand(n=1))
