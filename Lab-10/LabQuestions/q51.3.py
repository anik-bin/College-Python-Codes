# Consider a 16x16 array, how to get the blocksum (block size is 4x4)?

import numpy as np

Z = np.ones((16,16))
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)
print ('input array')
print (Z)
print ('block sum')
print (S)