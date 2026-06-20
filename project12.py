class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def introducing(self):
        return f"Robot Name: {self.name}|Battery Level: {self.battery}"


class WorkerRobot(Robot):
    def __init__(self, name, battery, task):
        super().__init__(name, battery)
        self.task = task

    def introducing(self):
        return f"Robot Name: {self.name}|Battery Level: {self.battery}|Task Type: {self.task}"


class GuardRobot(Robot):
    def __init__(self, name, battery, area):
        super().__init__(name, battery)
        self.area = area

    def introducing(self):
        return f"Robot Name: {self.name}|Battery Level: {self.battery}|Work Area: {self.area}"


team = []

while True:
    print("\n=== Robot Fleet Manager ===")
    print("1. Add Worker Robot")
    print("2. Add Guard Robot")
    print("3. Show All Robots")
    print("4. Save Fleet")
    print("5. Load Fleet")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Robot Name: ")
        battery = input("Battery Level: ")
        task = input("Task Type: ")
        worker = WorkerRobot(name, battery, task)
        team.append(worker)
        print("Worker robot added.")
    
    elif choice == "2":
        name = input("Robot Name: ")
        battery = input("Battery Level: ")
        area = input("Work Area: ")
        guard = GuardRobot(name, battery, area)
        team.append(guard)
        print("Guard robot added.")

    elif choice == "3":
        if not team:
            print("No robots in the fleet.")
        else:
            for robot in team:
                print(robot.introducing())

    elif choice == "4":
        import json
        data = []
        for robot in team:
            if isinstance(robot, WorkerRobot):
                data.append({"type": "worker", "name": robot.name, "battery": robot.battery, "task": robot.task})
            elif isinstance(robot, GuardRobot):
                data.append({"type": "guard", "name": robot.name, "battery": robot.battery, "area": robot.area})
        with open("fleet.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Fleet saved!")

    elif choice == "5":
        import json
        try:
            with open("fleet.json", "r") as file:
                data = json.load(file)
            team = []
            for r in data:
                if r["type"] == "worker":
                    team.append(WorkerRobot(r["name"], r["battery"], r["task"]))
                elif r["type"] == "guard":
                    team.append(GuardRobot(r["name"], r["battery"], r["area"]))
            print("Fleet loaded!")
        except:
            print("No saved fleet found")
            
    elif choice == "6":
        break

    else:
        print("Invalid option. Please choose a number from 1 to 6.")