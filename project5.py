class Robot:
    def __init__(self, name, mission):
        self.name = name
        self.mission = mission
        self.active = True

    def status(self):
        state = "active" if self.active else "inactive"
        print(f"{self.name} | Mission: {self.mission} | Status: {state}")
team = []

while True:
    print("\n1. Add a robot")
    print("2. Show team ")
    print("3. Quit")
    print("4. Deactivate a robot")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Robot name: ")
        mission = input("Robot mission: ")
        
        team.append(Robot(name, mission))
    elif choice == "2":
        for robot in team:
            robot.status()

    elif choice == "3":
        break
    elif choice == "4":
        name = input("Enter the name of the robot to deactivate: ")
        for robot in team:
            if robot.name == name:
                robot.active = False
                print(f"{name} has been deactivated!")