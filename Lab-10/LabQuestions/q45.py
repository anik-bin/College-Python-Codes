# How to find the most frequent value in a numpy array?

import numpy as np

a= np.array([0,1,2,3,1,2,1,1,1,3,2,2])

counts = np.bincount(a)
print(np.argmax(counts))