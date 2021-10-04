from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """La classe BoxWindow crée une"""

    def __init__(self, bounds):
        """La méthode init prend en argument les dimensions et crée une box window.
        On crée l'attribut bounds de la classe BoxWindow.

        Args:
            args ([type]): [description]
        """
        """On pourrait vérifier que bounds est de la forme nx2"""

        self.bounds = np.array(bounds)

    def __str__(self):
        """BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        b = "BoxWindow: "
        for i in range(self.bounds.shape[0]):
            b = b + f"{self.bounds[i]} x "
        return b[:-3]

    def shape(self):
        """Méthode qui permet de connaître la dimension de la box. La dimension est la shape de l'array. Dimension de bounds * 2.
        Le premier return permet d'avoir la première dimension."""
        return f"{self.bounds.shape[0]} x 2"

    def indicator_function(self, point):
        """Point in box ? """
        """ On pourrait vérifier que le point est à la bonne dimension, il doit être de la même taille que les bounds. On peut le faire avec un assert"""

        """ on peut itérer sur l'objet directement, pas de range(len(...))"""
        a = True
        for i in range(self.bounds.shape[0]):
            if (self.bounds[i, 0] <= point[i]) and (point[i] <= self.bounds[i, 1]):
                a == True
            else:
                return False
        return a

    def dimension(self):
        """"""
        return {self.bounds.shape[0]}

    def lenght(self):
        "This method return the lenght for each dimension of the BoxWindow."

        l = []
        for i in range(self.bounds.shape[0]):
            l = l + [self.bounds[i, 1] - self.bounds[i, 0]]
        return l

    def volume(self):
        """ It returns the lenght if the BoxWindow has 1 dimension, an area if 2 dimensions and the volume for 3 dimensions"""

        if self.dimension == 1:
            return f"Lenght = {self.lenght()[0]}"
        elif self.dimension == 2:
            return f"Area =  {self.lenght()[0] * self.lenght()[1]}"
        else:
            return f"Volume =  {self.lenght()[0] * self.lenght()[1] * self.lenght()[2]}"

    def indicator_functionseveral(self, args):
        """ Fonction indicatrice d'un ensemble, on veut avoir en entrée plusieurs points et que la fonction nous renvoie une liste avec True, False, True etc , si le point est dans la box ou non.

        Args:
            args ([type]): [description]
        """
        a = []
        for i in range(len(args)):
            a = a + [self.contains(args[i])]

        return a

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
        super(UnitBoxWindow, self).__init__(bounds)
