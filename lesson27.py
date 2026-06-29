# Simple Decorator
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result
    return wrapper

# Using the Decorator
@log_action
def move_robot(direction):
    print(f"Robot moving: {direction}")

@log_action
def charge_battery(level):
    print(f"Charging to: {level}%")

# Running
move_robot("forward")
print("---")
charge_battery(100)