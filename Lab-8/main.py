# object oriented programming in python

# class is a blueprint for real world entities

# object is an instance of a class

# class Aniket:
#     name = "Aniket"
#     roll = 20051196
#     cgpa = [9.3, 9.2, 9.1, 9.0]
#     marks = [100, 99, 98, 97]

#     def display(self):
#         print("Hello", self.name)
#         print("Your roll no is", self.roll)
#         print("Your cgpa are", self.cgpa)
#         print("Your marks are", self.marks)
        
# obj = Aniket()
# print(obj.name)
# obj.display()

# create a class with 2 variables and display the sum

# class addition:
#     # x = 50
#     # y = 60.9

#     def __init__(self):
#         self.x = int(input("Enter a value: "))
#         self.y = int(input("Enter a value: "))
#         print("result is:", self.x + self.y)


# obj = addition()

# create a class employee and display name, id, age, salary using paramterized constructor

# class employee:
#     def __init__(self):
#         self.name = input("Enter name: ")
#         self.id = int(input("Enter employee id: "))
#         self.age = int(input("Enter age: "))
#         self.salary = int(input("Enter salary: "))

#     def display(self):
#         print("\nEmployee details are: ")
#         print("Employee name: ", self.name)
#         print("Employee id is: ", self.id)
#         print("Employee age is: ", self.age)
#         print("Employee salary is: ", self.salary)

# obj1 = employee()
# obj1.display()

class employee:
    def __init__(self):
        self.a = []
        self.b = []
        self.c = []
        self.d = []

        for i in range(1, 6):
            print("Enter details for employee ", i)
            name = input("Enter name: ")
            id = int(input("Enter id: "))
            age = int(input("Enter age: "))
            salary = int(input("Enter salary: "))

            self.a.append(name)
            self.b.append(id)
            self.c.append(age)
            self.d.append(salary)
            


    def display(self):
        print("\nEmployee details are: ")
        print("Employee name: ", self.a)
        print("Employee id is: ", self.b)
        print("Employee age is: ", self.c)
        print("Employee salary is: ", self.d)

obj1 = employee()
obj1.display()