# Extract all the contiguous 3x3 blocks from a random 10x10 matrix.

import numpy as np
arra1 = np.random.randint(0,5,(10,10))
print("Original arrays:")
print(arra1)
n = 3
i = 1 + (arra1.shape[0]-3)
j = 1 + (arra1.shape[1]-3)
result = np.lib.stride_tricks.as_strided(arra1, shape=(i, j, n, n), strides = arra1.strides + arra1.strides)
print("\nContiguous 4x4 blocks:")
print(result)