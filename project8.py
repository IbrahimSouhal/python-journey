# Project 8: Robot Command System - Applying Data Flow Between Functions
def get_command(direction):
    """Convert direction to motor command"""
    if direction == "forward":
        return "Move motors forward"
    elif direction == "backward":
        return "Move motors backward"
    elif direction == "left":
        return "Turn left motor only"
    elif direction == "right":
        return "Turn right motor only"
    else:
        return "Stop all motors"


def execute_command(command):
    """Execute the robot command"""
    print(f"Executing: {command}")

def check_battery(battery_level):
    """Check if battery is sufficient"""
    if battery_level > 20:
        return True
    else:
        return False

# Main program - User Input
while True:
    print("=== Robot Control System ===")
    battery = int(input("Enter battery level (0-100): "))
    direction = input("Enter direction (forward/backward/left/right): ").lower()

    if check_battery(battery):
        command = get_command(direction)
        execute_command(command)
    else:
        print("Battery too low! Please charge first.")