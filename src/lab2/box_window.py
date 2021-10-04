from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, bounds):
        """[summary]

        Args:
            args ([type]): [description]
        """
        # if (type(args) == np.ndarray) and (args.shape[1] == 2):
        #    self.bounds = args
        # else:
        # self.bounds = np.ndarray([[]])
        self.bounds = np.array(bounds)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        return ""

    def __len__(self):
        S = 0
        for segment in self.bounds:
            S += segment[1] - segment[0]
        return S

    def __contains__(self, point):
        return all(a <= x <= b for (a, b), x in zip(self.bounds, point))

        # point = (1.5, 6)
        # assert len(self) == len(point)
        # verite = True
        # for dim in self.bounds.shape[0]:
        #    liminf = self.bounds[dim][0]
        #    limsup = self.bounds[dim][1]
        #    verite = verite and (point[dim] < limsup) and (point[dim] > liminf)
        # return verite

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
        return point in self

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
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


print(box_2d_05().indicator_function((0, 1)))
