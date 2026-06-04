# Writing to a file
file = open("robots.txt", "w")
file.write("Atlas\n")
file.write("Spot\n")
file.write("Eagle\n")
file.close()

print("File saved!")

# Reading from a file
file = open("robots.txt", "r")
content = file.read()
file.close()

print(content)