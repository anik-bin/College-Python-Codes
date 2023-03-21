# WAP in python that has a class Rectangle with attribute length and breadth
# and a method area that returns the area of the rectangle.

class Rectangle:

    def __init__(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def area(self):
        ar = self.length*self.breadth
        print("Area of rectangle is:", ar)

obj1 = Rectangle()
obj1.area()