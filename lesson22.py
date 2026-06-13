import re
text = "Robot battery: 85% and temperature: 72C"

battery = re.search(r'\d+(?=%)', text)
print("Battery:", battery.group())

numbers = re.findall(r'\d+', text)
print("All numbers:", numbers)

email = "ibrahim@gmail.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")