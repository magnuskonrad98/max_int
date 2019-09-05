size = int(input("Enter size: "))

numbers = []

for _ in range(size):
    number = int(input("Enter a number: "))
    numbers.append(number)

max_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

print("Max value is: ", max_value)
