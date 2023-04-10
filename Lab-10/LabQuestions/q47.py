# How to replace all values greater than a given value to a given cutoff?

import numpy as np
x = np.array([[ 2, 1, 3], [ 4, 5, 6], [ 3, 2, 4 ]])
print("Original array:")
print(x)
print("Replace all elements of the said array with 4 which are greater than 4")
x[x > 4] = 4
print(x)