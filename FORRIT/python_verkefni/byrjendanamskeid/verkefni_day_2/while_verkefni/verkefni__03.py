low = int(input("Enter low: "))
high = int(input("Enter high: "))

total = 0

while low <= high:
    total += low
    low += 1

print("total sum: ", total)
print("low: ", low)
print("high: ", high)

