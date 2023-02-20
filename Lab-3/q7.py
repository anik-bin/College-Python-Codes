my_dict = {
    "Name": "aniket",
    "Age": 21,
    "Gender": "Male",
    "Country": "India"
}

value = "aniket"

if value in my_dict.values():
    print("Yes it exists")
else:
    print("It does not exist")