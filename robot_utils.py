def get_status(battery):
    if battery < 20:
        return "Critical"
    elif battery < 50:
        return "Low"
    else:
        return "Good"
    
def celcius_to_fahrenheit(c):
    return (c * 9/5) + 32

ROBOT_NAME = "Unitree G1"    