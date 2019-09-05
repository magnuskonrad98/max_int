low = int(input("Enter an integer: "))
high = int(input("Enter a higher integer: "))


while low <= high:
    a = low % 2
    if a!=0:
        print(low)
        low=low+2
    else:
        low=low+1



print("Done!")