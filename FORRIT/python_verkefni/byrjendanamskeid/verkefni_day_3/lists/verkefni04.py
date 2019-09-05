numbers = []
size = int(input("Enter size: "))
total = 0

for x in range(size):
    a = int(input("Enter a number: "))
    numbers.append(a)
    total += a

print("The average is: ", total / size)


