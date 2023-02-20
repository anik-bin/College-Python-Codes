# WAP to print the series as 3 5 7 11 13 17..........n, where n is given by user.

from math import sqrt
def series(num):
  count=0
  n=3
  while count < num:
    # define a flag variable
    prime_flag = True 
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            prime_flag = False
            break
    if prime_flag:
        print(n, end =" ")
        count = count + 1
    n = n + 1
N =int(input("Enter number of terms in series :"))
series(N)