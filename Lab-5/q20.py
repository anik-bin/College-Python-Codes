# WAP to form reverse pyramid of numbers for a given number. Ex. for number 4
# 1 2 3 4 3 2 1
# 1 2 3 2 1
# 1 2 1
# 1

def pattern_print(num):
  for i in range(num, 0, -1):
    for j in range(num-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

num = int(input("Enter a number: "))
pattern_print(num)