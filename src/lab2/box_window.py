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

    def indicator_function(self, point):
        """Gives the result of the indicator fonction of the BoxWindows given one point

        Args:
            args ([int]): 1 if the argument is inside the BoxWindow, else 0
        """
        if point in self:
            return 1
        return 0

    def indicator_function_multiple_points(self, array_points):
        nb_points = array_points.shape[1]
        indicator = []
        for i in range(nb_points-1):
            indicator.append(int(self.indicator_function(array_points[i])))
        return indicator
    
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
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        # super(BoxWindow, self).__init__(args)
