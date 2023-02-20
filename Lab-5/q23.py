# WAP to convert a decimal number into its equivalent number with base b. Decimal number and b are
# the user input.

def convert_to_base(decimal, base):
    if decimal == 0:
        return '0'

    digits = ''
    while decimal > 0:
        remainder = decimal % base
        digits = str(remainder) + digits
        decimal //= base

    return digits

decimal = int(input("Enter a decimal number: "))
base = int(input("Enter the base: "))

result = convert_to_base(decimal, base)
print(f"The equivalent number of {decimal} in base {base} is: {result}")