# WAPinpython that has a class Fraction with attributes numerator
# and denominator. Enter the values to the attributes and print the
# function in simplified forms.

from math import gcd
class Fraction:
    def __init__(self):
        self.numerator=int(input("Enter Numerator:"))
        self.denominator=int(input("Enter Denominator:"))
    def display(self):
        a=gcd(self.numerator,self.denominator)
        self.numerator=self.numerator // a
        self.denominator=self.denominator // a
        print("Simplified Form Numerator =",self.numerator)
        print("Simplified Form Denominator =",self.denominator)
obj1=Fraction()
obj1.display()