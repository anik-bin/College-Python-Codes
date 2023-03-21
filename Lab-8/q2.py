# WAP in python with class Employee that keeps a track of the number of
# employees in an organization and also stores their name, designation and
# salary details.

class Employee:
    def __init__(self):
        self.name = input("Enter name: ")
        self.designation = input("Enter designation: ")
        self.salary = input("Enter salary: ")

    def display(self):
        print("\nEmployee details are")
        print("Employee name is", self.name)
        print("Employee designation is", self.designation)
        print("Employee salary is", self.salary)

obj1 = Employee()
obj1.display()
    