# Python program to count even and odd numbers using lambda function.

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
oddnum = len(list(filter(lambda x: (x%2 != 0) , list1)))
evennum = len(list(filter(lambda x: (x%2 == 0) , list1)))
print("\nNumber of even numbers: ", evennum)
print("\nNumber of odd numbers: ", oddnum)