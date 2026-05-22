def choices(person):
    if person == "woman":
        return "makeup"
    elif person == "man":
        return "football"
    else:
        return "unknown"
print(choices("woman"))
print(choices("man"))
print(choices("robot"))    