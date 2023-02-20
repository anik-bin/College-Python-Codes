#def wish():
#    print("Welcome")
#    print("to karnival")
    
#wish()

# =============================================================================
# def sum_nos():
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))
#     sum = num1 + num2
#     print("Sum is: ",sum)
#     
# sum_nos()
# =============================================================================

# function with arguments

# =============================================================================
# def wish(univ):
#     print("We are in", univ)
#     
# wish("KIIT")
# 
# def sum_nos():
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))
#     sum = num1 + num2
#     return sum
#     
# print("Sum is: ",sum_nos())
# =============================================================================

# def sum(x1, x2):
#     return x1+x2

# sum(2, 4)
# print("sum is:", sum(2, 4))

# default values in fucntion

# def sum(x1=30,x2=90):
#     return x1+x2

# res = sum(50)
# print("sum is:",res)

# def student_info(name, cgpa):
#     print("Good morning", name)
#     print("Your cgpa is", cgpa)
# student_info("Aniket", 10)

## keyword argument

def student_info(name, cgpa):
    print(name)
    print(cgpa)
student_info(name="Aniket", cgpa=10)

def fruits(price,name,city):
    print(name, "is supplied from", city, "and per item cost is",price)
fruits(name="coconut",city="bbsr",price=50)

def display(*var):
    [print(i**2) for i in var]
display(24, 83, 23, 44)

## arbitary arguments *

# def wish(*val):
#     print("Hello",val[2])

# wish("aniket", "sonu", "monu")

## arbitary arguments **

def wish(**val):
    print("Hello",val['n2'])

wish(n1="aniket", n2="sonu", n3="monu")