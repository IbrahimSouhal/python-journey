class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def speak(self):
        return f"I am {self.name}"
    
    def status(self):
        return f"Battery level: {self.battery}%"
    
# Inheritance
class WorkerRobot(Robot):
    def __init__(self, name, battery, task):
        super().__init__(name, battery)
        self.task = task

    def speak(self):
        return f"I am {self.name} and I do {self.task}"

class GuardRobot(Robot):
    def __init__(self, name, battery, area):
        super().__init__(name, battery)
        self.area = area

    def speak(self):
        return f"I am {self.name} guarding {self.area}"

robots = [
    WorkerRobot("Atlas", 85, "Welding"),
    GuardRobot("Unitree", 90, "warehouse"),
    Robot("Basic Bot", 50)
]

for robot in robots:
    print(robot.speak())
    print(robot.status())
    print("---")