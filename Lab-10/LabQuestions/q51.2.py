# Given an arbitrary number of vectors, build the cartesia product (every combinations of every item).

import numpy as np

# create some sample vectors
v1 = np.array([1, 2])
v2 = np.array([3, 4])
v3 = np.array([5, 6])

# build the cartesian product
grid = np.meshgrid(v1, v2, v3, indexing='ij')
cartesian_product = np.stack(grid, axis=-1).reshape(-1, len(grid))

# print the cartesian product
print(cartesian_product)
