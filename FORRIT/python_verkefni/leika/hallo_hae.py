a = int(input("Enter a number: "))
b = int(input("In the power of: "))

total = 0

for x in range(0, b + 1):
    total = a**x
    print(a, "in the power of ", x, "is: ", total)

print("Done!")


