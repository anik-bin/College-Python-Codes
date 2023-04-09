# Convert a 1-D array to a 3-D array

import numpy as np

a1 = np.array([x for x in range(27)])

a2 = a1.reshape((3,3,3))

print(a2)
 