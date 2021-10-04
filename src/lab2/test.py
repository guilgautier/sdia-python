#
# ? this file would sit in the tests/lab2 folder wouldn't it

import numpy as np

from lab2.box_window import *  # ! no wildcard import, import specific functions

# uB = BallWindow([0, .3, 4, 0], 10)
# x = np.array([5, 13, 5.3, 4])
# print(uB.dist_to_center(x))

# print(x in uB)
# print(len(uB))
# print(uB)

uB = UnitBoxWindow(10, np.array([[2.5, 2.5]]))
print(uB.center())
