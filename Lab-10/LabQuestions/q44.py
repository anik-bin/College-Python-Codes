# How to sort a 2D array by a column

import numpy as np

Sample_array = np.array([[100, 101, 500, 104], [201, 202, 203, 204], [301, 300, 600, 307]])

Index = 2

Array_sort = Sample_array[Sample_array[:,Index].argsort()]

print("The original array is:","\n","\n", Sample_array, "\n")
print("The sorted array is:", "\n", "\n", Array_sort)