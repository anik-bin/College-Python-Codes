# How to replace all missing values with 0 in a numpy array?

import numpy as np

my_array = np.array([4, np.nan, 6, np.nan, 10, 11, 14, 19, 22])

my_array[np.isnan(my_array)] = 0

print(my_array)