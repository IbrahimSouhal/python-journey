import json

class Mission:
    def __init__(mission, name, area):
        mission.name = name
        mission.area = area

class Patrol(Mission):
    def __init__(mission, name, area, duration):
        super().__init__(name, area)
        mission.duration = duration

    def introducing(mission):
        return f"{mission.name} - {mission.area} - completed"

class Delivery(Mission):
    def __init__(mission, name, origin, to, item):
        mission.name = name
        mission.origin = origin
        mission.to = to
        mission.item = item

    def introducing(mission):
        return f"{mission.name} - {mission.origin} to {mission.to} - completed"

class Inspection(Mission):
    def __init__(mission, name, area, status):
        super().__init__(name, area)
        mission.status = status

    def introducing(mission):
        return f"{mission.name} - {mission.area} - {mission.status}"


def check_temperature(temperature):
    if temperature < 50:
        return "Normal"
    elif temperature > 80:
        return "Critical!"
    else:
        return "Warning"


def check_battery(battery):
    if battery > 50:
        return "Good"
    elif battery < 20:
        return "Low!"
    else:
        return "Moderate"


def check_distance(distance):
    if distance > 30:
        return "Moving forward"
    elif distance < 10:
        return "Stopping"
    else:
        return "Slowing"

team = []
sensor_log = []

while True:
    print("\n=== Robot Control Systeme ===")
    print("1. Start Mission")
    print("2. Check Sensors")
    print("3. View Mission History")
    print("4. Analyze Data")
    print("5. Exit")

    choice = input("Enter an option:")

    if choice == "1":
        while True:
            print("\nChose mission type:")
            print("1. Patrol")
            print("2. Delivery")
            print("3. Inspection")

            pick = input("Enter an option:")

            if pick == "1":
                name = "Patrol"
                area = input("Work Area:")
                duration = input("Duration:")
                team.append(Patrol(name, area, duration))
                print("Mission started!")
                print("Sensors readings...")
                print("Mission completed! Saved to robot_systeme.json")
                break

            elif pick == "2":
                name = "Delivery"
                origin = input("Choose a starting point")
                to = input("Choose the endpoint")
                item = input("Select item type")
                team.append(Delivery(name, origin, to, item))
                print("Mission started!")
                print("Sensors readings...")
                print("Mission completed! Saved to robot_systeme.json")
                break

            elif pick == "3":
                name = "Inspection"
                area = input("Work Area:")
                status = "completed"
                team.append(Inspection(name, area, status))
                print("Mission started!")
                print("Sensors readings...")
                print("Mission completed! Saved to robot_systeme.json")
                break

            else:
                print("Invalid option")

        data = []
        for mission in team:
            if isinstance(mission, Patrol):
                data.append({"type": "patrol", "name": mission.name, "area": mission.area, "duration": mission.duration})
            elif isinstance(mission, Delivery):
                data.append({"type": "delivery", "name": mission.name, "from": mission.origin, "to": mission.to, "item": mission.item})
            elif isinstance(mission, Inspection):
                data.append({"type": "inspection", "name": mission.name, "area": mission.area, "status": mission.status})
        with open("robot_systeme.json", "w") as file:
            json.dump(data, file, indent=4)

    elif choice == "2":
        temperature = float(input("Enter the temperature level:"))
        print(check_temperature(temperature))
        battery = float(input("Enter battery level:"))
        print(check_battery(battery))
        distance = float(input("Enter the distance to the obstacle:"))
        print(check_distance(distance))
        sensor_log.append({"temperature": temperature, "battery": battery, "distance": distance})

    elif choice == "3":
        if not team:
            print("No missions recorded")
        else:
            print("=== Mission History ===")
            for mission in team:
                print(mission.introducing())

    elif choice == "4":
        print("=== Data Analysis ===")
        print("Total missions:", len(team))
        if sensor_log:
            batteries = [entry["battery"] for entry in sensor_log]
            temperatures = [entry["temperature"] for entry in sensor_log]
            print("Average battery:", sum(batteries) / len(batteries))
            print("Max temperature:", max(temperatures))
        else:
            print("No sensor data available")

    elif choice == "5":
        break