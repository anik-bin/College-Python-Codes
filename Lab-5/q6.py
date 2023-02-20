## WAP to print all odd and even numbers separately within a given range. The range is input through user.

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

def evenodd(x1,y1):
    print("Even numbers are:" )
    for i in range(a,b+1):
        if i%2==0:
            print(i)
            
    print("Odd numbers are: ")
    for i in range(a,b+1):
        if i%2!=0:
            print(i)
            
evenodd(a, b)