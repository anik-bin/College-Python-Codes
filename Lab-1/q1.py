num1 = input("Enter number 1: ")
num1 = int(num1)
num2 = input("Enter number 2: ")
num2 = int(num2)

print("Welcome to the menu")

while True:
    print("\nMenu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = int(input("\nEnter choice: "))

    if choice == 1:
        print(num1 + num2)
        
    
    elif choice == 2:
        print(num1 - num2)
        
    
    elif choice == 3:
        print(num1 * num2)
        
    
    elif choice == 4:
        print(num1 / num2)
        
    
    elif choice == 5:
        print("Thank you see you again")
        break
    
    else:
        print("Incorrect choice")
    