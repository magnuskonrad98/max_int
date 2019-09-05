my_int = int(input("Enter a number: "))
count = 0

while my_int > 1:
    if my_int % 2 == 0:
        my_int = my_int / 2
    elif my_int % 2 == 1:
        my_int = (my_int * 3) + 1
    print(my_int, ", ", end=" ")
    count += 1
print()
print("Cool, that were", count, "numbers")

