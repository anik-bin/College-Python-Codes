# Write a Python program to rearrange positive and negative numbers in a given
# array using Lambda.

list_nums = [101,-2,-3,4,5,-6,7,-8,-9,10]
result = sorted(list_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)