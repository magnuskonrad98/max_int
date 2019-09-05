age_int = int(input("Enter your age: "))

if age_int < 35:
    print("Young")
elif age_int < 51:
    print("Mature")
elif age_int < 70:
    print("Middle-aged")
else:
    print("Old")