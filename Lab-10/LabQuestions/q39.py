# How to find the count of unique values in a numpy array?

import numpy as np

#create NumPy array
my_array = np.array([1, 3, 3, 4, 4, 7, 8, 8])
arr1 = len(np.unique(my_array))
print(arr1)