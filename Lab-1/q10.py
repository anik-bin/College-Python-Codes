height = float(input("Height of cylinder: "))
radian = float(input("Radius of cylinder: "))
pi=22/7
volume = pi * radian * radian * height
surface_area = ((pi*radian**2)*2) + ((2*pi*radian) * height)
print("Volume is: ", volume)
print("Surface Area is: ", surface_area)