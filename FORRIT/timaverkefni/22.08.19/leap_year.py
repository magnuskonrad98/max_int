year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year = True
        else:
            year = False
    else:
        year = True
else:
    year = False


print(year)

