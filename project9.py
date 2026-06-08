def get_temperature_status(temperature):
    if temperature > 80:
        return "Overheating! Cooling system activated."
    elif temperature < 50:
        return "Temperature low."
    else:
        return "Temperature normal."

def get_battery_status(battery):
    if battery < 20:
        return "Low battery! Returning to base."
    elif battery > 50:
        return "Battery good."
    else:
        return "Battery moderate."

def get_obstacle_status(distance):
    if distance < 10:
        return "Obstacle detected! Stopping."
    elif distance > 30:
        return "Path is clear.Moving forward."
    else:
        return "Object nearby!Slowing down."

print("=== Robot:Atlas ===")
temperature = float(input("Enter temperature: "))
battery = float(input("Enter battery level: "))
distance = float(input("Enter obstacle distance: "))

print(get_temperature_status(temperature))
print(get_battery_status(battery))
print(get_obstacle_status(distance))

file = open("sensor_log.txt", "w")
file.write("=== Reading ===\n")
file.write(f"Temperature: {temperature} | {get_temperature_status(temperature)}\n")
file.write(f"Battery: {battery} | {get_battery_status(battery)}\n")
file.write(f"Obstacle Distance: {distance} | {get_obstacle_status(distance)}\n")
file.write("-----------------\n")
file.close()