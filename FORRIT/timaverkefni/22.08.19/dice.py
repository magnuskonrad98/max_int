d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below

if not (d1 and d2 in range(1, 7)):
    print("Invalid input")
else:
    sum = d1 + d2
    if sum in [7, 11]:
        print("Winner")
    elif sum in [2, 3, 12]:
        print("Loser")
    else:
        print(sum)

