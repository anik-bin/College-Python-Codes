# WAP to check whether an input integer is strong number or not. (Hint: If the sum of factorials of all
# digits of a number are equal to the number are equal to the number, it is called a strong number )

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


def strong_num(x):
    sum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    if x == sum:
        print(x, "is a perfect number")
    else:
        print(x, "is not a perfect number")
    return ("")


num = int(input("Enter your number :"))
print((strong_num(num)))
