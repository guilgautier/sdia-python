from lab2.utils import get_random_number_generator


class BoxWindow:
    """[summary]
    """

    def __init__(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        self.bounds = None

    def __repr__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [type]: [description]
        """
        return ""

    def __len__(self):
        return

    def __contains__(self, args):
        return True or False

    def dimension(self):
        """[summary]
        """
        return

    def volume(self):
        """[summary]
        """
        return

    def indicator_function(self, args):
        """[summary]

        Args:
            args ([type]): [description]
        """
        return

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        return


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(BoxWindow, self).__init__(args)
