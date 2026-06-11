temperatures = [72, 45, 88, 31, 95, 60]
hight_temps = []
for t in temperatures:
    if t > 70:
        hight_temps.append(t)
print("Normal way:", hight_temps)

hight_temps2 = [t for t in temperatures if t > 70]
print("Comprehension:", hight_temps2)

celcius = [0, 20, 37, 100]
fahrenheit = [(c * 9/5) + 32 for c in celcius]
print("Fahrenheit:", fahrenheit)