# WAP to calculate the sum of digits of a given number.

def sum_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

num = int(input("Enter a number: "))
print(sum_digits(num))
