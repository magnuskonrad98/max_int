total = 0
my_int = int(input("Enter an integer: "))
largest_int = 0
odd_count = 0
even_count = 0

while my_int > 0:
    total += my_int
    print("Cumulative total:", total)
    if my_int % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if my_int > largest_int:
        largest_int = my_int
    my_int = int(input("Enter an integer: "))
    if my_int < 1:
        print("Largest number: ", largest_int)
        print("Count of even numbers: ", even_count)
        print("Count of odd numbers: ", odd_count)
        break


