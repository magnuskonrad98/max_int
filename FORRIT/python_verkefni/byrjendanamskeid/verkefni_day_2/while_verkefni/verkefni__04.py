low = int(input("Enter low: "))
high = int(input("Enter high: "))

total = 0

while low <= high:
    if low % 2 == 0:
        total += low
    low += 1

print("total sum: ", total)
print("low: ", low)
print("high: ", high)