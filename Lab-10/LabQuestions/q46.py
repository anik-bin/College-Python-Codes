# How to find the position of the first occurrence of a value greater than a given value?

import numpy as np

arr = np.array([1, 3, 2, 4, 5, 6])

idx = np.argwhere(arr > 3)[0]

print(idx)
