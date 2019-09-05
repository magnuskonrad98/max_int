size = int(input("Enter size: "))

numbers = []


for _ in range(size):
    number = int(input("Enter number: "))
    numbers.append(number)

print("The list is: ", numbers)
total = 0
for number in numbers:
    total += number

print("The sum of the list is:", total)

