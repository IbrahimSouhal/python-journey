robot = {
    "name": "Robo",
    "type": "AI",
    "purpose": "Assist humans",
    "mission": "Make life easier"
}
print(robot["name"])
print(robot["type"])
robot["mission"] = input("What is his mission? ")
print("Updated mission: " + robot["mission"])