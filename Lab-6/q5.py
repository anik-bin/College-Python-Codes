# Write a Python program to find if a given string starts with a given character
# using Lambda.

x = lambda x: True if x.startswith('P') else False
print(x('Python'))
x = lambda x: True if x.startswith('P') else False
print(x('Parrot'))