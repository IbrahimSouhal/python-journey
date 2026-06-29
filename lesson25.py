def robot_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid input type!"
    finally:
        print("Operation attempted.")

print(robot_divide(10, 2))
print(robot_divide(10, 0))
print(robot_divide(10, "a"))

# Custom Exception
class BatteryError(Exception):
    pass

def check_battery(level):
    if level < 0 or level > 100:
        raise BatteryError(f"Invalid battrey level: {level}")
    return f"Battery: {level}"

try:
    print(check_battery(85))
    print(check_battery(150))
except BatteryError as e:
    print(f"Battery Error: {e}")