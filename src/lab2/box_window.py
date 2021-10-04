from lab2.utils import get_random_number_generator

import numpy as np


class BoxWindow:
    """une classe utilisée pour représenter des pavés droit en dimension quelconque"""

    def __init__(self, bounds):
        """

        Args:
            bounds (numpy array): list of the box bounds'
        """

        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        string = "BoxWindow: "
        dim = self.dimension()
        i = 0

        for list in self.bounds:

            a = list[0]
            b = list[1]
            if a.dtype == "float64" and a.is_integer():
                a = int(a)
            if b.dtype == "float64" and b.is_integer():
                b = int(b)

            if i == dim - 1:
                string += "[" + str(a) + ", " + str(b) + "]"

            else:
                string += "[" + str(a) + ", " + str(b) + "]" + " x "
            i += 1

        return string

    def __len__(self):
        """returns the max length of the box sides'

        Returns:
            [numerical type]: max length of the box sides'
        """
        return np.max(np.array([b - a for [a, b] in self.bounds]))

    def __contains__(self, point):
        """tell if a given point is contained in the box

        Args:
            point (numpy array): list of the coordinates of the point

        Returns:
            [boolean]: True if the point is in the box, False otherwise
        """
        assert len(point) == self.dimension()
        bounds = self.bounds
        dim = self.dimension()
        for i in range(dim):
            if not bounds[i][0] <= point[i] <= bounds[i][1]:
                return False

        return True

    def dimension(self):
        """returns the number of dimensions of the box

        Returns:
            [numerical type]: number of dimensions of the box
        """
        return len(self.bounds)

    def volume(self):
        """compute the volume of the box

        Returns:
            [numerical type]: volume of the box
        """
        V = 1
        for [a, b] in self.bounds:
            V *= b - a
        return V

    def indicator_function(self, point):
        """compute the indicator function of the space delimited by the box at a given point

        Args:
            point (numpy array): coordinates of the point

        Returns:
            [boolean]: value of the indicator function
        """
        return point in self

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): number of point to generate. Defaults to 1.
            rng ([type], optional): np.random.Generator instance. Defaults to None.

        Returns:
            [numpy list]: list of the generated points
        """

        rng = get_random_number_generator(rng)
        pointArray = np.array(
            [[rng.random() * (b - a) + a for [a, b] in self.bounds] for i in range(n)]
        )
        return pointArray

    def center(self):
        """returns the center point of the box

        Returns:
            [numpy list]: center point
        """
        return np.array([(a + b) / 2 for [a, b] in self.bounds])


class UnitBoxWindow(BoxWindow):
    def __init__(self, center):
        """subclass of BowWindow for boxes with all sides equal to 1

        Args:
            center (numpy list): list of the coordinates of the central point of the box
        """
        bounds = np.array([[c - 0.5, c + 0.5] for c in center])
        super(UnitBoxWindow, self).__init__(bounds)


class BallWindow:
    """a class used to represents balls in any dimension"""

    def __init__(self, center, radius):
        """

        Args:
            center (numpy list): list of the coordinates of the center of the ball
            radius (numerical type): radius of the ball
        """

        self.center = center
        self.radius = radius

    def __str__(self):
        r"""

        Returns:
            [type]: [description]
        """
        string = "BallWindow: "
        dim = self.dimension
        string += "center: " + str(self.center) + "radius: " + str(self.radius)

        return string

    def __len__(self):
        """returns the diamter of the ball

        Returns:
            [numerical type]: diameter
        """
        return 2 * self.radius

    def __contains__(self, point):
        """tell if a given point is contained in the ball

        Args:
            point (numpy array): list of the coordinates of the point

        Returns:
            [boolean]: True if the point is in the ball, False otherwise
        """

        assert len(point) == self.dimension()
        dim = self.dimension()
        d = 0
        for i in range(dim):
            d += (self.center[i] - point[i]) ** 2

        return d <= self.radius ** 2

    def dimension(self):
        """returns the number of dimensions of the ball

        Returns:
            [numerical type]: number of dimensions of the ball
        """
        return len(self.center)

    def volume(self):
        """compute the volume of the box

        Returns:
            [numerical type]: volume of the box
        """
        n = self.dimension()
        R = self.radius
        if n % 2 == 0:
            V = np.pi ** (n // 2) * R ** n / np.math.factorial(n // 2)
        else:
            V = (
                2
                * np.math.factorial(n // 2)
                * (4 * np.pi) ** (n // 2)
                * R ** n
                / np.math.factorial(n)
            )
        return V

    def indicator_function(self, point):
        """compute the indicator function of the space delimited by the ball at a given point

        Args:
            point (numpy array): coordinates of the point

        Returns:
            [boolean]: value of the indicator function
        """

        return point in self
