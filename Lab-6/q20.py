# # Write a Python program to convert a given list of tuples to a list of strings
# using the map function.

def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result   
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConverted:")
print(tuples_to_list_string(colors))

