data = {
    "sub":"T&T",
    "sem":6,
    "Dept":"CSE-7"        
}

print(data)
print(data.keys())
print(data.values())

for val in data:
    print(val)
    
for x in data:
    print(data[x])
    
for x in data.values():
    print(x)
    
for x in data.items():
    print(x)
    
for d, e in data.items():
    print(d, ":", e)
    
data["sub"] = "Tools & Techniques"
print(data)

data["campus"] = 14
print(data)

data["sub"] = ["TT", "CD", "ML"]
print(data)

for x in data["sub"]:
    print(x)
    
# read a string and display frequency of each character in that

