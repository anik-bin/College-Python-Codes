num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if(num1 > num2):
    min1 = num1
else:
    min1 = num2
while(True):
    if(min1 % num1 == 0 and min1 % num2 == 0):
        print("LCM is:",min1)
        break
    min1=min1+1