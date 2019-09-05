low = int(input("Enter low: "))
high = int(input("Enter high: "))

total = 0

for number in range(low, high + 1):
    if number % 2 == 0:
        total += number

print("The total is: ", total)


