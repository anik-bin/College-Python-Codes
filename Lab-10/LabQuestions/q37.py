# How to find if a given array has any null values?

import numpy as np

arr = np.array([1, 2, 3, 4, np.NaN, 5, 6])

if(np.isnan(arr).any()):
    print("The Array contain NaN values")
else:
    print("The Array does not contain NaN values")