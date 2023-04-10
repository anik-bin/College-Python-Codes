# How to find the position of missing values in numpy array?

import numpy as np 
 
nums = np.array([[3, 2, np.nan, 1],
              [10, 12, 10, 9],
              [5, np.nan, 1, np.nan]])

print("Original array:") 
print(nums)
print("\nPosition of missing data of the said array:")
print(np.argwhere(np.isnan(nums)))