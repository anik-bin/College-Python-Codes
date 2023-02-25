bases_num = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Base numbers and index: ")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("\nResult:")
print(result)