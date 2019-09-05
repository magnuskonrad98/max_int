num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
sum_of_integers = 0

while num != 10:
    sum_of_integers += num
    num = int(input("Input an int: "))
else:
    print(sum_of_integers)