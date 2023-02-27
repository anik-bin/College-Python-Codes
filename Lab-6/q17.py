# # Write a Python program to convert a given list of integers and a tuple of
# integers in a list of strings.

nums_list = [1,2,3,4]
nums_tuple = (0, 1, 2, 3) 
result_list = list(map(str,nums_list))
result_tuple = list(map(str,nums_tuple))
print("\nList of strings:")
print(result_list)
print("\nTuple of strings:")
print(result_tuple)
