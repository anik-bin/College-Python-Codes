# WAP to convert a number with base b into its equivalent decimal number. Number with base b & b are
# the user input.

def convert_to_decimal(num, base):
    decimal = 0
    power = 0
    while num > 0:
        digit = num % 10
        decimal += digit * (base ** power)
        power += 1
        num //= 10
    return decimal

num = int(input("Enter the number: "))
base = int(input("Enter the base of the number: "))

decimal = convert_to_decimal(num, base)
print("The decimal equivalent of", num, "in base", base, "is:", decimal)