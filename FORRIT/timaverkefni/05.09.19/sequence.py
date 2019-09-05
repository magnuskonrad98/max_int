n = int(input("Enter the length of the sequence: ")) # Do not change this line

sum_of_numbers = 0
number_1 = 1
number_2 = 0
number_3 = 0
for x in range(1, n+1):
    number_3 = number_2
    number_2 = number_1
    number_1 = sum_of_numbers
    sum_of_numbers = number_1 + number_2 + number_3
    print(sum_of_numbers)

