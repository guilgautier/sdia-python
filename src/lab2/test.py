from lab2.box_window import *
import numpy as np

bounds = np.array([[0., 5.], [-1.45, 3.14], [-10., 10.]])

bounds = np.array([[0., 1.], [-2, 3], [0., 10.]])

for dim in bounds:
    print(dim)

b = BoxWindow(bounds)
print(b)
print(len(b))

print(b.volume())

x = np.array([[0., 5.]])

print()
