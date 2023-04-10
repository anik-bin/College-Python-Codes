# How to filter a numpy array based on two or more conditions?

import numpy as np

Sample_array = np.array([55,60,65,70,75,80,85,90])

filter_array = []

for values in Sample_array:
  if values > 65:
    filter_array.append(True)  
  else:
    filter_array.append(False) 

new_filtered_array = Sample_array[filter_array]

print("The filtered array is:", new_filtered_array)