# How to convert an array of arrays into a flat 1d array?

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

flat_arr = np.concatenate(arr)

print(flat_arr)
