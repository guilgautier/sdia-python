from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[summary]"""

    def __init__(self, boundsArg):
        """Initialize the BoxWindows from the bounds given in the array.

        Args:
            args (array): array of bounds containing the coordinates of each bound
        """
        self.bounds = np.array(boundsArg)

    def __str__(self):
        """Display the BoxWindow in a string

        Returns:
            [string]: BoxWindows points coordinates
        """
        description = "BoxWindow: "
        for i in range(len(self.bounds)):
            description = description + str(list(self.bounds[i])) + " x "
        return description[:-3]

    def __len__(self):
        """Returns the dimension of the space of the BoxWindow

        Returns:
            [int]: size of the space containing the BoxWindow
        """
        return self.bounds.shape[0]

    def __contains__(self, point):
        """Indicates whether the argument given is inside the Box Window of not.
        Assertion error if the dimension of the point is not equal to the dimension of the BoxWindow

        Args:
            point (np.array): [list of coordinates]

        Returns:
            [boolean]: [True if the point is inside, else returns False]
        """
        assert len(point) == len(self) ##Test if the point has the same dimension
        dim = len(self)
        for i in range(dim):
            a = self.bounds[i, :]
            if a[0] > point[i] or a[1] < point[i]:
                return False 
        return True

    def dimension(self):
        """[summary]"""
        return len(self)

    def volume(self):
        """Gives the volume of the BoxWindow

        Returns:
            [int]: [volume]
        """
        dim = len(self)
        volume = 1
        for i in range(0, dim):
            long = abs(self.bounds[i][0] - self.bounds[i][1])
            volume = volume * long
        return volume

    def indicator_function(self, array_points):
        """Gives the result of the indicator function of the BoxWindows given some points of the same dimension

        Args:
            args ([int]): 1 if the argument is inside the BoxWindow, else 0
        """
        if len(array_points.shape) > 1:
            return [int(p in self) for p in array_points]
        return int(array_points in self)

    
    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        
        Returns:

        """
        dim = len(self)
        #for i in range(dim):
            
        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """Initialize a BoxWindow which is centered around the center given (default = 0) 
        and in the dimension given (default = 2)

        Args:
            dimension ([int]): dimension expected of the BoxWindow
            center ([type], optional): . Defaults to None.
        """
        bounds = np.zeros((dimension, 2))
        bounds[:, 0], bounds[:, 1] = center - 0.5, center + 0.5
        super(UnitBoxWindow, self).__init__(bounds)
    
    ##Remarque sur la fonction : le center est un entier !! or en dim 2, on devrait avoir deux coordonnées
    
