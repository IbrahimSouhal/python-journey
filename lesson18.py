robot = {
    "name": "Atlas",
    "status": "active",
    "sensors": {
        "temperature": 72,
        "battery": 85,
        "distance": 23
    }
}

print(robot["name"])
print(robot["sensors"]["temperature"])

robot["sensors"]["battery"] = 60
print(robot["sensors"]["battery"])

for key, value in robot["sensors"].items():
    print(f"{key}: {value}")