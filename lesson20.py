def double(x):
    return x * 2

print(double(5))

double2 = lambda x: x * 2
print(double2(5))

status = lambda battery: "Low" if battery < 20 else "Good"
print(status(15))
print(status(80))

sensors = [72, 45, 88, 31, 95]
sorted_sensors = sorted(sensors, key=lambda x: x)
print("Sorted:", sorted_sensors)