# # Write a Python program to convert all the characters into uppercase and
# lowercase and eliminate duplicate letters from a given sequence. Use the map()
# function.

def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'A', 'B', 'a', 'e', 'i', 'o', 'u'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting:")
print(set(result))
