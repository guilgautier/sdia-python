#
# todo same remarks as in box_window
class BallWindow:
    # ! naming: radIUs
    def __init__(self, center, raduis):
        """initialization

        Args:
            center (list): the center
            raduis (float): raduis of the ball
        """
        self.center = center
        self.raduis = raduis

    def __str__(self):
        """print the ball

        Returns:
            str: BallWindow: center=..., raduis=...
        """
        return (
            "BallWindow: "
            + "center="
            + str(self.center)
            + ", raduis="
            + str(self.raduis)
        )

    def indicator(self, point):
        r"""True if the point in the ball

        Args:
            point (list): point
        Returns:
            bool: True if the point in the ball
        """

        s = 0
        for i in range(self.dimension):
            s += (point[i] - self.center[i]) ** 2
        if s <= self.raduis ** 2:
            return True
        return False

    def dimension(self):
        """the dimension of the ball

        Returns:
            int: dimension
        """
        return len(self.center)
