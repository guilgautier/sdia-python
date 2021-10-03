from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, bounds):
        """La méthode init prend en argument les dimensions et crée une box window.
        On crée l'attribut bounds de la classe BoxWindow

        Args:
            args ([type]): [description]
        """
        """On pourrait vérifier que bounds est de la forme nx2"""

        self.bounds = np.array(bounds)


    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        box="BoxWindow "
        for i in range (len(self.bounds)):
        return ""

    def __len__(self):
        """Méthode qui permet de connaître la dimension de la box. La dimension est la shape de l'array. Dimension de bounds * 2.
        Le premier return permet d'avoir la première dimension."""
        return self.bounds.shape[0]
        return len(self.bounds)

    def __contains__(self, point):
        """Point in box ? """
        """ On pourrait vérifier que le point est à la bonne dimension, il doit être de la même taille que les bounds. On peut le faire avec un assert"""
        assert len(point) == len(self)

        """ on peut itérer sur l'objet directement, pas de range(len(...))"""

        for (a,b), x in zip(self.bounds, point):
            if not (a <= x <= b):
                return False
        return True


        a= self.bounds[:, 0]
        b=self.bounds[:, 1]
        return np.all (np.logical_and(a <= point, point <= b))


        return(all(a <= x <= b for (a,b), x in zip(self.bounds, point)))





    def dimension(self):
        """"""
        return

    def volume(self):
        """[summary]"""
        return

    def indicator_function(self, args):
        """ Fonction indicatrice d'un ensemble, on veut avoir en entrée plusieurs points et que la fonction nous renvoie une liste avec True, False, True etc , si le point est dans la box ou non.

        Args:
            args ([type]): [description]
        """
        return

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
