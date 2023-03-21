# WAP in python that has a class Person storing name and date of birth of a person.
# The program should subtract the date of birth from today’s date to find out that the
# person is eligible to vote or not.

import datetime

class Person():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def display(self):
        today = datetime.date.today()
        age = today.year-self.dob.year
        if age >= 18:
            print(self.name,"is eligible to vote")
        else:
            print(self.name,"not eligible to vote")


p = Person("Aniket", datetime.date(2001, 8, 17))
p.display()
