# WAP to print the following pattern for n rows. Ex. for n=5 rows
# *
# * *
# * * *
# * * * *
# * * * * *

def patter_print(n):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

rows = int(input("Enter number of rows: "))
patter_print(rows)