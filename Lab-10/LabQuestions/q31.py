# How to find the percentile scores of a numpy array?
import numpy as np

# Array of data
arr = [5,6,9,87,2,3,5,7,2,6,5,2,3,4,69,4]

# Finding the 90 percentile 
x = np.percentile(arr, 90)
print(x)