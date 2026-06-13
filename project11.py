import json

temperature = float(input("Enter temperature: "))
battery = float(input("Enter battery level: "))
distance = float(input("Enter obstacle distance: "))

if distance < 10:
    status = "Critical"
elif distance > 30:
    status = "Path is clear. Moving forward."
else:
    status = "Object nearby! Slowing down."

robot = {
    "readings": [
        {
            "temperature": temperature,
            "battery": battery,
            "distance": distance,
            "status": status
        }
    ]
}

while True:
    another = input("Add another reading? (yes/no): ")
    if another == "no":
        break

try:
    with open("robot_log.json", "r") as file:
        data = json.load(file)
    
except:
    data = {"readings": []}

data["readings"].append(robot["readings"])

with open("robot_log.json", "w") as file:
    json.dump(data, file, indent=4)

print(f"Total readings: {len(data['readings'])}")