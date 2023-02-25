list1 = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
result = list(filter(lambda x: (x == "".join(reversed(x))), list1)) 
print("\nList of palindromes:")
print(result) 