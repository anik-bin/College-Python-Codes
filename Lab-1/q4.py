import math
print("Enter Time:")

h1=int(input("Hour : "))
m1=int(input("Minute : "))
s1=int(input("Second : "))

print("Enter Time:")
h2=int(input("Hour : "))
m2=int(input("Minute : "))
s2=int(input("Second : "))

print("Time 1 :",h1,":",m1,":",s1)
print("Time 2 :",h2,":",m2,":",s2)
h3=h1+h2+(m1+m2+(s1+s2)/60)/60
m3=(m1+m2+(s1+s2)/60)%60
s3=(s1+s2)%60
print("Total Time  :",math.floor(h3),":",math.floor(m3),":",math.floor(s3))