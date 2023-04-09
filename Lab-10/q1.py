# Given are 2 similar dimensional numpy arrays, how to get a numpy array output in which every
# element is an element-wise sum of the 2 numpy arrays?

import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array([5, 6, 7, 8])

a3 = np.add(a1, a2)
print(a3)