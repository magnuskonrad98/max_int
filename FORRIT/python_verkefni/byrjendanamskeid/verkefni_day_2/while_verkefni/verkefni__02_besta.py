low = int(input("Enter low: "))
high = int(input("Enter high: "))

while low <= high:
    if low % 2 == 1:
        print(low)
        low = low + 2
    else:
        low = low + 1


print("Done!")