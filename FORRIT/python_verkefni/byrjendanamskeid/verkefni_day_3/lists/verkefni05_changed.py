size = int(input("Enter a size: "))
numbers = []



for _ in range(size):
    number = int(input("Enter a number: "))
    numbers.append(number)
    min_value = numbers[0]
    if number < min_value:
        min_value = number

print("Min value is: ", min_value)

