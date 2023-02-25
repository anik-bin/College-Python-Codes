# Write a Python program to create Fibonacci series up to n using Lambda.

from functools import reduce
n = int(input("Enter value of n: "))
fibo_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
print("Fibonacci series upto",n,":")
print(fibo_series(n))