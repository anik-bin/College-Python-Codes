# How to get the positions of top n values from a numpy array?

import numpy as np

scores = np.array([100,67,92,87,66,89,76,22])

x = np.argsort(scores)[::-1][:3]
print("Indices:",x)

print("Values:",scores[x])