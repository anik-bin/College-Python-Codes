# How to find the correlation between two columns of a numpy array?

import numpy as np

rng = np.random.default_rng(seed=9)
xarr = rng.integers(low=0, high=10, size=(3, 3))
print(xarr)

r1 = np.corrcoef(xarr)
# print(r1)

yarr = rng.integers(low = 0, high=10, size=(3, 3))
# print(yarr)

r2 = np.corrcoef(yarr)
# print(r2)

r3 = np.corrcoef(xarr, yarr, rowvar=False)
print(r3)