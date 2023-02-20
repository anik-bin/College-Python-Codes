n = int(input("Enter value of n: "))

sum = sum([i*(i+1)/2 for i in range(1, n+1)])

print("Sum is:", int(sum))