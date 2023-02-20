# WAP to print the following pattern for n rows. Ex. for n=6 rows
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
# 0 1 0 1 0 1

def print_pattern(n):
  for i in range(n):
    for j in range(i+1):
        if (i+j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
n = int(input("Enter the number of rows: "))
print_pattern(n)