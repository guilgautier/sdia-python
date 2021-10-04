from lab2.utils import get_random_number_generator
import numpy as np
import matplotlib.pyplot as plt


class BoxWindow:
    """[summary]"""
    def __init__(self, args):
        """Create bow window

        Args:
            args (list of N float array): [a, b] bounds for each of the N dimensions of the window box.
        """
        self.bounds = args

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: string representation of the box window.
        """
        l_str = list(map(lambda x: f"[{x[0]}, {x[1]}]", self.bounds))
        return "BoxWindow: " + " x ".join(l_str)

    def __len__(self):
        return len(self.bounds)

    def in_segment(self, x, segment):
        """Tool function indicating if a point is in a given segment or not.

        Args:
            x (float array): point of interest
            segment (float array): segment considered

        Returns:
            bool: True if point is in the segment else False
        """
        return segment[0] <= x < segment[1]

    def __contains__(self, x):

        return all(a <= x <= b for (a, b), x in zip(self.bounds, x))

    def dimension(self):
        """Returns the number of dimension of the window box

        Returns:
            int: number of dimensions.
        """
        return len(self)

    def volume(self):
        """Returns the volume of the window box defined as the product of size of each dimension.

        Returns:
            float: volume of the window box.
        """
        v = 1
        for dim in self.bounds:
            v *= np.abs(dim[0] - dim[1])
        return v

    def indicator_function(self, args):
        """Returns if args is in the window box.

        Args:
            args (float array): The window box [description]

        Returns:
            bool: True if point in window box, else False.
        """
        return args in self

    def get_random_point_inside(self):
        """Returns a point at random in the window box

        Returns:
            float array: random point in the bow window
        """

        return np.array([np.random.uniform(*dim) for dim in self.bounds])

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return [self.get_random_point_inside()] * n

    def center(self):
        """Compute center of the box window.

        Returns:
            float array: center coordinates of the box window.
        """
        mid = lambda x: (x[0] + x[1]) / 2
        c = list(map(mid, self.bounds))
        return np.array(c)


class UnitBoxWindow(BoxWindow):
    def __init__(self, dimension, center):
        """Unit box of a given dimension (hypercube box) at a given center point

        Args:
            dimension (float): [description]
            center (float array, optional): center of the window.
        """

        bounds = np.array([[c - dimension / 2, c + dimension / 2]
                           for c in center])
        print(bounds)

        super(UnitBoxWindow, self).__init__(bounds)


class BallWindow:
    def __init__(self, center, radius):
        """Create new ball window.

        Args:
            center (float array): coordinates of the center of the ball window.
            radius (float): radius of the ball window.
        """
        self.center = center
        self.radius = radius

    def dist_to_center(self, x):
        """Compute the distance of a given point to the center of the ball window.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            float: distance of the given point to the center of the ball window.
        """
        return np.sqrt(np.sum(np.power(x - self.center, 2)))

    def dist_to_ball(self, x):
        """Compute the distance of a given point to the surface of the ball window.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            float: distance of the given point to the surface of the ball window.
        """
        return self.dist_to_center(x) - self.radius

    def __contains__(self, x):
        """Compute whether a given point is contained in the ball window or not.

        Args:
            x (float array): coordinates of the point of interest.

        Returns:
            bool: point is in ball window or not.
        """

        # we need to compute the distance of the point of interest to the center of the ball window
        return self.dist_to_center(x) < self.radius

    def __str__(self):
        """BallWindow: (center, radius)

        Returns:
            str: string representation of the ball window.
        """
        return f"BallWindow (center : {self.center}, radius : {self.radius})"

    def __len__(self):
        """Indicates the number of dimension of the ball window.

        Returns:
            int: number of dimension of the ball window.
        """
        return len(self.center)

    def volume(self):
        """Computes the volume of the ball.

        Returns:
            float: volume of the ball window.
        """

        return 4 * np.pi * np.power(self.radius, 3) / 3


def estimate_pi(n=int(1e5)):
    """Estimating pi using the rejection sampling method

    Args:
        n (int, optional): number of iterations for pi estimation. Defaults to int(1e5).
    Returns:
        float list: list of all estimations of pi (last should be the more accurate)
    """
    center = np.array([0, 0])

    ball = BallWindow(center, 1)
    unit_box = UnitBoxWindow(2, center)

    c = 0
    rslt = []
    for i in range(n):
        c += unit_box.get_random_point_inside() in ball
        rslt += [4 * c / (i + 1)]
    return rslt


if __name__ == '__main__':
    # Estimating pi using the rejection sampling method
    plt.plot(estimate_pi(), label="estimated pi")
    plt.title("Estimation of pi over iterations")
    plt.legend()
    plt.show()
