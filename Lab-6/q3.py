# Write a Python program to filter a list of integers 9odd and even) using
# Lambda.

list1 = [1,2,3,4,5,6,7,8,9,10]
print("\nList of even numbers:")
evenNumbers = list(filter(lambda x: x%2 == 0, list1))
print(evenNumbers)
print("\nList Odd numbers:")
oddNumbers = list(filter(lambda x: x%2 != 0, list1))
print(oddNumbers)