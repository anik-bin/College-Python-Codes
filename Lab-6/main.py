# Lambda function

# Lambda is known as anonymous function or namesless function
# used for writing single line of code
# takes any number of arguments but only one expression
# find square of a number using function

# def square_no(x):
#     return x**3

# sqr = square_no(4)
# print("Square is:", sqr)

# find square of a number using lambda function

square = lambda a:a**2
print(square(4))

cube = lambda b:b*b*b
print(cube(5))

city = ['delhi', 'mumbai', 'bhubaneswar', 'kolkata']
city.sort(key=lambda x:len(x))
print(city)

# map function

# find square of numbers from a list

list1 = [4, 5, 6, 7, 8, 9]

# method 1

sqr = []
for item in list1:
    sqr.append(item*item)

print(sqr)

# method 2 list comprehension

list2 = [x**2 for x in list1]
print(list2)

# method 3 using function

def find_square(my_list):
    list3 = [i**2 for i in my_list]
    return list3

find_square(list1)


# method 4 map function
# syntax: map(function, iterables)
# iterables: list., tuple, set, array, dict, string

res = map(lambda x:x**3, [4, 8, 12, 16])

print(list(res))

# find area of 5 circles using map and lambda

import math

area = map(lambda r:round(r*r*math.pi,3), (5, 6, 7, 8, 9))
print(tuple(area))

# display even numbers froma list

# method 1 using function

list4 = [4, 7, 16, 34, 64]
list5 = []
def check_even(mylist):
    for item in mylist:
        if item % 2 == 0:
            print(item, end=' ')

check_even(list4)

# method 2 using map function
val = map(lambda x:(x%2==0), list4)
print(list(val))

# method 3 using filter
# filter function syntax: filter(user_defined function, iterables)
# filer function syntax 2: filter(lambda function, iterables)

odd_nos = filter(lambda a:(a%2==1), [23, 7, 16, 4, 9])
print(list(odd_nos))

# Reduce function

# declare two lists and find the sum using function

# def sum_of_two_lists(x1, x2):
#     for i in range(len(x1)):
#         print(x1[i] + x2[i])

# list1 = [3, 4, 6, 7]
# list2 = [4, 8, 16, 32]
# sum_of_two_lists(list1, list2)

def sum_of_two_lists(x1, x2):
    sum_list = list(map(lambda x,y: x+y,x1,x2))
    return sum_list

list1 = [3, 4, 6, 7]
list2 = [4, 8, 16, 32]
print(sum_of_two_lists(list1, list2))

import functools
list6 = [1,2,3,4]
def func(b,c):
    return b+c
print(functools.reduce(func, list6))