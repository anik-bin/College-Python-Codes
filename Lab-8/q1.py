# WAP in python that uses class to store the name and marks of the students. Use
# list to store the marks in three subjects.

class Students:
    name = "Aniket"
    marks = [20, 30, 40]

    def display(self):
        print("Name is", self.name)
        print("Marks are", self.marks)
        
obj1 = Students()
obj1.display()
