low = int(input("Enter low: "))
high = int(input("Enter high: "))

total = 0

for number in range(low, high + 1):
    print("number is now: ", number)
    print("the total + number is now: ", total, " + ", number, " = ", total+number)
    total += number
    #or total = total + number

print("The sum is: ", total)

