list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

res = list(filter(lambda x: x in list1, list2)) 
print ("\nIntersection of the arrays: ",res)