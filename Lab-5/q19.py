# WAP to print the following pattern for n rows. Ex. for n=5 rows
# 1
# 2 1
# 1 2 3
# 4 3 2 1
# 1 2 3 4 5

def print_pattern(n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(i+1):
                print(j+1, end=" ")
        else:
            for j in range(i,-1,-1):
                print(j+1, end=" ")
        print()

n = int(input("Enter the number of rows: "))
print_pattern(n)