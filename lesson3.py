user = {
    "name": "Ibrahim",
    "age": 15,
    "city": "Beni Mellal",
    "dream": "Robotic Engineer"
}

print(user["name"])
print(user["dream"])
user["city"] = input("Enter your city: ")
print("updated city: " + user["city"])