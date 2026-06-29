# Simple Gnerator
def sensor_readings(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# Usage
for reading in sensor_readings(1, 5):
    print(f"Reading: {reading}")

# Robot Data Generator
def battery_simulator(start, drain):
    battery = start
    while battery > 0:
        yield battery
        battery -= drain

print("\n--- Battery Simulation ---")
for level in battery_simulator(100, 15):
    print(f"Battery: {level}%")
    if level <= 15:
        print("Low Battery")
        break