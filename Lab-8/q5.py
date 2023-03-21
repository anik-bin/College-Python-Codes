# WAP in python that has a class Student that stores the name ,roll no, marks(in
# three subjects). And display the information(name, roll no, total marks) stored
# about the students.

class Student:
    
    def __init__(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))
        self.c = []
        for i in range(0, 3):
            marks = int(input("Enter marks: "))
            self.c.append(marks)

    def display(self):
        print("Student name is:", self.name)
        print("Student roll number is:", self.roll)
        print("Student total marks are:", sum(self.c))

obj1 = Student()
obj1.display()

    