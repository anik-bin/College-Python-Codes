# WAP in python that has a class Circle. Use a class variable that defines the
# value of constant Pie value=3.14. Use this class variable to calculate the
# area and circumference of the circle with specifiedradius.

class circle:
    x = 3.14

    def __init__(self):
        self.r = int(input("Enter Radius:"))

    def circumference(self):
        cir = 2*self.x*self.r
        print("Circumference is:", cir)

    def area(self):
        ar = self.x*self.r*self.r
        print("Area is:", ar)


obj1 = circle()
obj1.circumference()
obj1.area()
