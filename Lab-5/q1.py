## WAP to calculate the factorial of a given number.
def factorial_num():
    num = int(input("Enter a number: "))    
    factorial = 1      
    for i in range(1,num + 1):    
        factorial = factorial*i    
    print("Factorial is",factorial)

factorial_num()