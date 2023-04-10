# How to compute the row wise counts of all possible values in an array?

import numpy as np

arr = np.array([[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]])

unique_vals = np.unique(arr)

arr_2d = arr.reshape(-1, 1)

counts = np.apply_along_axis(lambda x: np.bincount(x, minlength=len(unique_vals)), axis=1, arr=arr_2d)

counts = counts.reshape(arr.shape[0], -1)

print(counts)

# output

# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]