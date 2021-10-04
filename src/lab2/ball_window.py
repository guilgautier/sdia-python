import numpy as np


class BallWindow:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __len__(self):
        return len(self.center)

    def __contains__(self, point):
        return

    def dimension(self):
        return

    def volume(self):
        return

    def indicator_function(self):
        return

    def rand(self, numberOfPoints):
        return
