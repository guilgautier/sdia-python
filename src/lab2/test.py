from lab2.box_window import *
import numpy as np

uB = BallWindow([0, .3, 4, 0], 10)
x = np.array([5, 13, 5.3, 4])
print(uB.dist_to_center(x))

print(x in uB)
print(len(uB))
print(uB)
