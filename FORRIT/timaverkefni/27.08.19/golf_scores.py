count = 1

while count <= 18:
    par = int(input(f"Par of hole {count}: "))
    score = int(input(f"Score on hole {count}: "))
    x = score - par
    if x < -3:
        print("invalid score")
    elif x == -3:
        print("albatross")
    elif x == -2:
        print("eagle")
    elif x == -1:
        print("birdie")
    elif x == 0:
        print("par")
    elif x == 1:
        print("bogey")
    elif x == 2:
        print("double bogey")
    elif x == 3:
        print("triple bogey")
    else:
        print("bad hole")
    count += 1
