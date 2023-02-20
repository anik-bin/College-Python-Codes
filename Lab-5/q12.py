# WAP to print the series as 1 2 7 15 31 ..........n, where n is given by user.

def print_series(n):
    num = 1
    for i in range(n):
        print(num, end=" ")
        num = num * 2 + 1

n = int(input("Enter the number of terms: "))
print_series(n)