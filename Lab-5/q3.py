def mean_marks(mar):
    average = sum(mar)/len(mar)
    return average
def grade_marks(g):
    if g>=80:
        print("E")

    elif g>=70:
        print("A")

    elif g>=60:
        print("B")

    else:
        print("Back")
marks=[90, 91, 89, 88, 87, 84]
avg = mean_marks(marks)
grade_marks(avg)