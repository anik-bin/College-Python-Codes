# Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in
# 2D arrays)

import numpy as np

a1 = np.array([[1,2,3], [4,5,6]])

a2 = np.array([[7,8,9], [10,11,12]])

a3 = np.hstack((a1, a2))

print(a3)