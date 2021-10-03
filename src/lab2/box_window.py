from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]
    """

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
        args = self.bounds
        hamza = ""
        for i in range(0, len(args)):
            hamza = hamza + str(args[i])
            if i < len(args) - 1:
                hamza += " x "

        return "BoxWindow : " + hamza

    def __len__(self):
        args = self.bounds
        return len(args)

    def __contains__(self, args):
        Box_args = self.bounds
        for i in range(0, len(arg)):
            a = args[i][0]
            b = args[i][1]
            c = box_args[i][0]
            d = box_args[i][1]
            if a < c or d < b:
                return False
        return True

    def dimension(self):
        """[summary]
        """
        n = len(self.bounds)
        return 2 * n

    def volume(self):
        """[summary]
        """
        n = len(self.bounds)
        args = self.bounds
        V = 1
        for i in range(0, n):
            l = args[i][1] - args[i][0]
            v = v * l
        return v

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        Box_args = self.bounds
        n = len(Box_args)
        for i in range(0, n):
            a = Box_args[i][1]
            b = Box_args[i][0]
            if args[i] < b or arg[i] > a:
                return False
        return True

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        n = len(self.bounds)
        args = self.bounds
        L = []
        for i in range(0, n):
            a = random.uniform(args[i][0], args[i][1])
            L.append(a)
        L = np.array(L)
        return L

    def center(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        center = []
        n = len(self.bounds)
        for i in range(n):
            b_i = self.bounds[i][1]
            a_i = self.bounds[i][0]
            center.append((b_i + a_i) / 2)
        return center


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        L = []
        for i in range(dimension):
            L.append([center[i] - 0.5, center[i] + 0.5])
        super().__init__(L)

class BallWindow(BoxWindow):
    def __init__()
