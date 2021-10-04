# from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, bounds):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = np.array(bounds)

    def __str__(self):
        """BoxWindow: `[a_1, b_1] x [a_2, b_2] `

        Returns:
            [type]: [description]
        """
        bounds_list = []
        if len(self.bounds.shape) == 1:
            return "BoxWindow: " + str(self.bounds.tolist())

        A_list = self.bounds.tolist()
        to_print = ""
        for i in range(len(A_list)):
            if i != len(A_list) - 1:
                to_print = to_print + str(A_list[i]) + " x "
            else:
                to_print = to_print + str(A_list[i])

        return "BoxWindow: " + to_print

    def __len__(self):
        S = 0
        for segment in self.bounds:
            S += segment[1] - segment[0]
        return S

    def __contains__(self, point):

        for i in range(len(point)):
            if not (self.bounds[i][0] <= point[i] <= self.bounds[i][1]):
                return False
        return False

    def dimension(self):
        """[On donne la dimension mathématique de la boite]"""
        return self.bounds.shape[0]

    def volume(self):
        produit = 1
        for segment in self.bounds:
            longueur = segment[1] - segment[0]
            produit *= longueur
        return produit

    def indicator_function(self, point):
        """[summary]

        Args:
            args ([type]): [description]
        """
        verite = self.__contains__(point)
        return verite

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


# a = BoxWindow([[1, 2], [5, 8]])
# print((0.5, 6) in a)
# def box_2d_05():
# return BoxWindow(np.array([[0, 5], [0, 5]]))


# print(box_2d_05().indicator_function((0, 4)) == True)
# print(box_2d_05().__contains__((np.array([2.5, 2.5]))))
