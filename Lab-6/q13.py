# Write a Python program to add three given lists using Python map and
# lambda.

def sum_of_three_lists(x1, x2, x3):
    sum_list = list(map(lambda x,y,z: x+y+z,x1,x2,x3))
    return sum_list

list1 = [3, 4, 6, 7]
list2 = [4, 8, 16, 32]
list3 = [10, 20, 30, 40]
print(sum_of_three_lists(list1, list2, list3))