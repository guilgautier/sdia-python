from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """Représentation de [x,y] x [x1,y1] x ... x [xn,yn] """

    def __init__(self, L):
        """Construit l'objet

        Args:
            args np.array([[x,y],[x1,y1],...,[xn,yn]]): np.array d'intervalle dans chaque dimension
        """
        self.bounds = L

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            String : "BoxWindow: [a_1,b_1] x [a_2,b_2] x ..."
        """
        S = "BoxWindow: "
        for i in range(len(self.bounds)):
            S += "[" + str(self.bounds[i][0]) + ", " + str(self.bounds[i][1]) + "]"
            if i != len(self.bounds) - 1:
                S += " x "
        return S

    def __len__(self):
        """dimension"""
        return len(self.bounds)

    def __contains__(self, point):
        for i, x in enumerate(point):
            print(self.bounds[i][0], x, self.bounds[i][1])
            if not (self.bounds[i][0] <= x <= self.bounds[i][1]):
                return False
        return True

    def dimension(self):
        """[summary]"""
        return len(self)

    def volume(self):
        """[summary]"""
        res = 1
        for i in range(len(self.bounds)):
            longueur = np.sqrt((self.bounds[i][1] - self.bounds[i][0]) ** 2)
            res = res * longueur
        return res

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
        L = np.array((n, 2))
        for i in range(n):
            P = []
            for j in range(self.dimension()):
                P.append("")
        return L


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
