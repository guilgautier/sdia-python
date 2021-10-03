import numpy as np

from lab2.utils import get_random_number_generator


class BoxWindow:
    """Creates a window of rectangular shape"""

    def __init__(self, args):
        """initialize the box window with the bounding points

        Args:
            args (np.array([integer])): array of the bounding points of the box
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str : give the bounds of the box
        """
        mot = ""
        for [a, b] in self.bounds:
            mot = mot + str([a, b]) + " x "
        return "BoxWindow: " + mot[:-3]

    def __len__(self):
        """
        Returns:
            list : list of the length in each direction
        """
        L = []
        for (a, b) in self.bounds:
            L.append(b - a)
        return L

    def __contains__(self, point):
        """Indicates if the point is contained in the box window.
        Returns True if the point is in the box, returns False otherwise.

        Args:
            point ([np.array([Integer])): coordonnées d'un point
        """
        for (a, b), x in zip(self.bounds, point):
            if not (a <= x <= b):
                return False
        return True

    def dimension(self):
        """
        Returns:
            integer : dimension of the box
        """
        return len(self.bounds)

    def volume(self):
        """
        Returns:
            integer : volume of the box
        """
        vol = 1
        for p in self.__len__():
            vol = vol * p
        return vol

    def indicator_function(self, args):
        """Indicator function of the box window. Returns 1 if the point is in the box, returns 0 otherwise.

        Args:
            args ([np.array([Integer])): coordonnées d'un point
        """
        if self.__contains__(args) == True:
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

        L = []
        for p in range(n):
            L_petit = []
            for (a, b) in self.bounds:
                if a == b:
                    L_petit.append(a)
                else:
                    L_petit.append(np.random.uniform(b - a) + a)
            L.append(L_petit)
        return L


# heritage
class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
