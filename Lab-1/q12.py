n = int(input("Enter the number: "))
list = []
sum = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
           break
    else:
        sum = sum + i
print("The sum of the prime numbers are:", sum)