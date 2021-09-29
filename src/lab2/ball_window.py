from lab2.utils import get_random_number_generator
import numpy as np


class BallWindow:
    """fenetre ronde
    """

    def __init__(self, centre, rayon):
        """[summary]

        Args:
            centre (Liste): Point qui centre la fenetre
            rayon (int): rayon de la fenetre
            """

        self.rayon = rayon
        self.centre = centre

    def __str__(self):
        """affiche le centre et le rayon de la fenetre
        """

        return (
            "BallWindow de centre: "
            + str(self.centre)
            + " et de rayon: "
            + str(self.rayon)
        )

    def __len__(self):
        """renvoie la dimension du centre
        """
        return len(self.centre)

    def __contains__(self, point):
        """dit si le point est dans la fenetre

        Args:
            point (Array): point de l'ensemble
        """
        dist = 0
        for i, x in point:
            dist += (x - self.centre[i]) ** 2
        return np.sqrt(dist) <= self.rayon

    def dimension(self):
        """renvoie la dimension de la fenetre
        """
        return len(self)

    def volume(self):
        """volume/aire/longueur de la BallWindow

        Returns:
            int: volume/aire/longueur
        """
        assert len(self) <= 3
        if len(self) == 3:
            return (4 * np.pi * self.rayon ** 3) / 3
        elif len(self) == 2:
            return np.pi * self.rayon ** 2
        else:
            return 2 * self.rayon

    def indicator_function(self, point):
        """return the image of the point through the indicator function described by the bow window

        Args:
            args ([type]): [description]
        """
        return self.__contains__(point)

        ###########
        # On pourrait continuer avec les autres fonctions (rand,..)
        ###########
