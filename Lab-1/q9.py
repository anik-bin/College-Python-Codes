number = int(input ("Enter the number: "))      
count = 1
i = 0   
print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number * 1
    i = i+1  
    print (number, 'x', i, '=', number * count)    
    count += 1