name = input("Enter your name: ")
weight = float(input("Enter your weight in kgs: "))

if weight > 90:
    print(name, " competes in heavyweight")

elif weight <= 90 and weight >= 60:
    print(name, " competes in middleweight")

else:
    print(name, " competes in lightweight")


