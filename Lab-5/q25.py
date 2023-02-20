# WAP to convert a binary number to its equivalent octal & hexa-decimal number system.

def convert_binary(num):
    # Convert binary to decimal
    decimal = 0
    for digit in num:
        decimal = decimal * 2 + int(digit)

    # Convert decimal to octal
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8

    # Convert decimal to hexadecimal
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
        decimal //= 16

    return octal, hexadecimal

num = input("Enter a binary number: ")

octal, hexadecimal = convert_binary(num)

print("The equivalent octal of", num, "is", octal)
print("The equivalent hexadecimal of", num, "is", hexadecimal)