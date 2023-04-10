# How to drop rows that contain a missing value from a numpy array?

import numpy as np

a = np.array([[1,2,np.nan], [4,5,6]])
b = a[~np.isnan(a).any(axis=1)]
print(b)