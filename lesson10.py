from turtle import speed


class Robot:
    def __init__(self, name, mission):
        self.name = name
        self.speed = speed

    def introduce(self):
        print(f"I am {self.name}")

class FlyingRobot(Robot):
    def __init__(self, name, speed, max_height):
        super().__init__(name, speed)
        self.max_height = max_height
    def fly(self):
        print(f"{self.name} is flying at {self.max_height} meters.")

robot1 = Robot("Atlas", 10)
robot2 = FlyingRobot("Eagle", 50, 1000)

robot1.introduce()
robot2.introduce()
robot2.fly()