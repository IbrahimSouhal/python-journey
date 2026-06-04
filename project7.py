import os

class Robot:
    def __init__(self, name, mission):
        self.name = name
        self.mission = mission


def save_team(team):
    with open("team.txt", "w") as file:
        for robot in team:
            file.write(f"{robot.name},{robot.mission}\n")
    print("team saved!")


def load_team():
    team = []
    if os.path.exists("team.txt"):
        with open("team.txt", "r") as file:
            for line in file:
                name, mission = line.strip().split(",")
                team.append(Robot(name, mission))

    return team


if __name__ == "__main__":
    team = load_team()

    while True:
        print("\n1. Add Robot")
        print("2. Show team")
        print("3. Save and Quit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter robot name: ")
            mission = input("Enter robot mission: ")
            team.append(Robot(name, mission))

        elif choice == "2":
            for robot in team:
                print(f"{robot.name} | {robot.mission}")

        elif choice == "3":
            save_team(team)
            break