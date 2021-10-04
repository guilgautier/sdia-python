import numpy as np
import numpy.linalg as la
from math import gamma
from lab2.utils import get_random_number_generator


class BallWindow:
    """Creates a Ball window, meaning a volume around a center point with a radius"""

    def __init__(self, center, radius=1.0):
        """Initialize the BallWindows from the center and the radius

        Args:
            center (list) : gives the coordinates of the center 
            radius (int) : gives the radius of the ball. Default to 1.
        """
        self.center = np.array(center)
        self.radius = float(radius) 

    def __str__(self):
        """Display the BallWindow in a string

        Returns:
            [string]: BallWindows center and radius 
        """
        description = "BallWindow: center" + str(list(self.center)) + " & radius[" + str(self.radius) + "]."
        return description

    def __len__(self):
        """Returns the dimension of the space of the BallWindow

        Returns:
            [int]: size of the space containing the BallWindow
        """
        return self.center.shape[0]

    def __contains__(self, point):
        """Indicates whether the argument given is inside the Ball Window of not.
        Assertion error if the dimension of the point is not equal to the dimension of the BallWindow

        Args:
            point (np.array): [list of coordinates]

        Returns:
            [boolean]: [True if the point is inside, else returns False]
        """
        assert len(point) == len(self) ##Test if the point has the same dimension
        return la.norm(self.center - point) <= self.radius

    def dimension(self):
        """Gives the dimension of the BallWindow"""
        return len(self)

    def volume(self):
        """Gives the volume of the BallWindow

        Returns:
            [int]: [volume]
        """
        n = self.dimension()
        R = self.radius
        return (np.pi ** (n / 2) * R ** (n)) / gamma(1 + n / 2)

    def indicator_function(self, array_points):
        """Gives the result of the indicator function of the BallWindows given some points of the same dimension

        Args:
            args ([int]): 1 if the argument is inside the BallWindow, else 0
        """
        if len(array_points.shape) > 1:
            return np.array([int(p in self) for p in array_points])
        return int(array_points in self)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BallWindow`.

        Args:
            n (int, optional): Number of random points to generate. Defaults to 1.
            rng (type, optional): Defaults to None.
        
        Returns: array which contains n points randomly uniformly generated

        """ 
        dim = len(self)           
        rng = get_random_number_generator(rng)
        r = self.radius
        res = rng.uniform(0, 1, (n, dim))
        normalis = np.apply_along_axis(np.linalg.norm, axis= 0, arr=res)
        res = res / normalis 
        dist = rng.uniform(-r, r, (n, 1) )
        res = res * dist 
        return res + self.center  
    