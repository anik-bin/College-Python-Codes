""""
WAP to check whether a number n is prime number or not. /*Hints: A number is a perfect number if is
equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself.
Write a function to check if a given number is perfect or not. The first perfect number is 6, because 1, 2,
and 3 are its proper positive divisors, and 1 + 2 + 3 = 6*/
"""

num=int(input("Enter Number: "))
def prime_no():
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
                break
    else:
        print(num,"is not a prime number")
def perfect_no():
    my_sum = 0
    for i in range(1, num):
        if(num % i == 0):
            my_sum = my_sum + i
    if (my_sum == num):
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")
prime_no()
perfect_no()