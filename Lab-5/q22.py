# WAP to display the following style o/p for a given string input through keyboard.(Ex.for a string
# “KIITCSIT”)

# KIITCSITTISCTIIK
# KIITCSI ISCTIIK
# KIITCS SCTIIK
# KIITC CTIIK
# KIIT TIIK
# KII IIK
# KI IK
# K K
# KI IK
# KII IIK
# KIIT TIIK
# KIITC CTIIK
# KIITCS SCTIIK
# KIITCSI ISCTIIK
# KIITCSITTISCTIIK

def print_pattern(size):
    for i in range(size, 0, -1):
        for j in range(0, i):
            print(s[j], end='')
        
        for j in range(0, size - i):
            print(' ', end='')
        
        for j in range(0, size - i):
            print(' ', end='')
        
        for j in range(i - 1, -1, -1):
            print(s[j], end='')
        print()

    for i in range(2, size + 1):
        for j in range(0, i):
            print(s[j], end='')
        
        for j in range(0, size - i):
            print(' ', end='')
        
        for j in range(0, size - i):
            print(' ', end='')
        
        for j in range(i - 1, -1, -1):
            print(s[j], end='')
        print()

s = input('Enter a string: ')
size = len(s)
print_pattern(size)