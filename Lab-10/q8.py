# Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)

import numpy as np

a1 = np.array([[1,2], [3,4], [5,6]])

a2 = np.array([[7,8], [9,10], [10,11]])

a3 = np.vstack((a1, a2))

print(a3)