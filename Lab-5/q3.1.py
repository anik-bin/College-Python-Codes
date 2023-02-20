## WAP to display the reverse of a number entered through keyboard.

def reverse_num(n):
    r=0
    while n>0:
        digit=n%10
        r=(r*10)+(digit)
        n=n//10
    return r

num = int(input("Enter a number: "))
print(reverse_num(num))