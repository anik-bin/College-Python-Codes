# # Write a Python program to create a new list taking specific elements from a
# tuple and convert a string value to an integer.

student_data  = [('Aniket Bindhani','17/08/2001','75kg'), ('Sonu','17/05/2002','65kg'), ('Marcel Wellington','16/02/1999', '52kg'), ('Lucy Olives','25/09/1998', '72kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student dob:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)
