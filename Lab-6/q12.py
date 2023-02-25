# Write a Python program to triple all numbers in a given list of integers. Use
# Python map and lambda.

list1=[1,2,3,4,5]
result=list(map(lambda x:x*3, list1))
print(result)