# How to get the second largest value of an array when grouped by another array?

import numpy as np

values = np.array([3, 4, 5, 1, 2, 6, 7, 8, 9])
groups = np.array([1, 1, 2, 2, 2, 3, 3, 3, 3])

sorted_values = np.sort(values)[::-1]

group_indices = np.unique(groups, return_index=True)[1]

second_largest = [sorted_values[group_indices[i]+1] for i in range(len(group_indices)-1, -1, -1)]

print(second_largest)
