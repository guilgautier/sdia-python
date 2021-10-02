from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]BoxWindow class representing a virtual n-dimensional bounded Box
    """

    def __init__(self, args):
        """[summary]Initialization of Box's parameters

        Args:
            args ([numpy array list]): [this argument represents the bounds of the box]
        """
        self.bounds = args

    def __str__(self):
        """[summary] BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [str]: [description of the Box's bounds]
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

        representation = (
            representation
            + "["
            + str((self.bounds)[shape[0] - 1][0])
            + ", "
            + str((self.bounds)[shape[0] - 1][1])
            + "]"
        )

        return representation

    def __len__(self):
        """[summary]

        Returns:
            [int: [the dimension of the box]
        """
        return ((self.bounds).shape)[0]

    def __contains__(self, args):
        """[summary]This method tests if an element (args) is inside the box

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the box , False if not]
        """
        flag = True
        for i in range(self.__len__()):
            if args[i] >= self.bounds[i][0] and args[i] <= self.bounds[i][1]:
                flag = True
            else:
                return False

        return flag

    def dimension(self):
        """[summary]
        This method is similar to the method __len__ described above
        """
        return self.__len__()

    def volume(self):
        """[summary]
        This method calculates the volume of the Box
        """
        v = 1
        for i in range(self.dimension()):
            v = v * abs((self.bounds[i][1] - self.bounds[i][0]))

        return v

    def indicator_function(self, args):
        """[summary]
        This method is similar to the method  __contains__  described above

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the box , False if not]
        """
        if self.__contains__(args):
            return True
        else:
            return False

    def center(self):
        """[summary] determinate the center of the box

        Returns:
            [numpy array list]: [the center of the box]
        """
        c = np.zeros(self.__len__())
        for i in range(self.__len__()):
            c[i] = np.mean(self.bounds[i])
        return c

    def rand(self, n=1, rng=None):
        """[summary]
        Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.

        Returns:
            Randomly n elements that belong to the box
        """
        rng = get_random_number_generator(rng)
        L = np.ones((n, self.__len__()))  # liste des points

        for i in range(n):
            for j in range(self.__len__()):
                x = rng.random()

                L[i][j] = (1 - x) * self.bounds[j][0] + x * self.bounds[j][1]

        return L


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]a subclass of BoxWindow,represents the notion of "unit square box"

        Args:
            dimension ([int]): [dimension of the Unit Box]
            center ([numpy array list], optional): [center of the Box].
        """
        self.bounds = np.array(
            [[center[i] - 0.5, center[i] + 0.5] for i in range(dimension)]
        )
        super().__init__(self.bounds)


class BallWindow:
    """[summary]BoxWindow class representing a virtual n-dimensional bounded Box
    """

    def __init__(self, center, radius, dimension):
        """[summary]Initialization of Box's parameters

        Args:
            args ([numpy array list]): [this argument represents the bounds of the box]
        """
        self.dim = dimension
        self.rad = radius
        self.cent = center

    def __contains__(self, args):
        """[summary]This method tests if an element (args) is inside the ball

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the ball , False if not]
        """
        flag = True
        if len(args) != self.dim:
            return False
        else:
            if np.linalg.norm(args - self.center) <= self.rad:
                flag = True

        return flag

    def dimension(self):
        """[summary]
        This method gives the dimension of the ball
        """
        return self.dim

    def volume(self):
        """[summary]
        This method calculates the volume of the Ball using the formula :math:' $V_{n+1} =\int_{-r}^{r}V_{n}(\sqrt{r^2 -x^2})dx$ '
        """

        v = 1
        for i in range(self.dimension()):
            integ = lambda x: v * np.sqrt(self.rad ** 2 - x ** 2)
            v = integrate.quad(integ, -self.rad, self.rad)

        return v

    def indicator_function(self, args):
        """[summary]
        This method is similar to the method  __contains__  described above

        Args:
            args ([numpy array list]): [the element to test]

        Returns:
            [bool]: [True if the element is inside the ball , False if not]
        """
        if self.__contains__(args):
            return True
        else:
            return False

    def center(self):
        """[summary] determinate the center of the ball

        Returns:
            [numpy array list]: [the center of the ball]
        """
        c = np.zeros(self.__len__())
        for i in range(self.__len__()):
            c[i] = np.mean(self.bounds[i])
        return c
