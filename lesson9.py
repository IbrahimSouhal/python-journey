class  robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def introduce (self):
        print(f"My name is {self.name} and my speed is {self.speed} km/h.")

robot1 = robot("Atlas", 10)
robot2 = robot("Spot", 5)

robot1.introduce()
robot2.introduce()