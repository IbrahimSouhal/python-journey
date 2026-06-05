def get_robot_status(battery_level):
    """Check robot battery status"""
    if battery_level > 50:
        return "Ready"
    elif battery_level > 20:
        return "Low Battery"
    else:
        return "Needs Charging"

def display_status(status):
    """Display robot status"""
    print(f"Robot Status: {status}")

# Main program
current_battery = 35
status = get_robot_status(current_battery)
display_status(status)