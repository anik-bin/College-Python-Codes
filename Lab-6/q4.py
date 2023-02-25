# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

list1 = [1,2,3,4,5,6,7,8,9,10]
print("\nList of squared numbers:")
squaredNumbers = list(map(lambda x: x**2, list1))
print(squaredNumbers)
print("\nList of Cubed numbers:")
cubedNumbers = list(map(lambda x: x**3, list1))
print(cubedNumbers)