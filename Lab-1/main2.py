import math
name = "aniket is good"
name2 = name.upper()
print(name2)
print(name)
print(name[5:10])

txt = "Kiit Deemed Univ"
txt = txt.replace("Deemed", "deemed")
print(txt)

# Read a num from keyboard and find out square root of that number



#Loop
MyList = []
'''while(True):
     num = input("Enter a number ")
     if(not num):
         print("Invalid Input")
         break
     if(num.isdigit()):
         num = int(num)
         MyList.append(math.sqrt(num))
        # print("The square root is: ", )
     else:
         MyList.append(len(num))
         #print("Length is:", )
         
print("The entire output is: ", MyList)'''
         
#List

con = [1, 12, 3, 4, 12, 8 , 9]
con.count(12)
for ele in con:
    if ele == 12:
        con.remove(ele)
print(con)
