import json
robot = {
    "name": "UnitreeG1",
    "battery": 85,
    "sensors": {
        "temperature": 72,
        "distance": 23

    }
}

json_string = json.dumps(robot, indent=4)
print(json_string)

with open("robot_data.json", "w") as f:
    json.dump(robot, f, indent=4)

with open("robot_data.json", "r") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["sensors"]["temperature"])