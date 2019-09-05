number_str = input("Enter a number, and when you are tired just enter a period (.): ")
the_sum = 0

while number_str != ".":
    number = int(number_str)
    if number % 2 == 1:
        number_str = input("Gaddem you, only even numbers. Enter an even number: ")
        continue
    else:
        the_sum += number
    number_str = input("Enter a number: ")

print("The sum is: ", the_sum)