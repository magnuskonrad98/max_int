n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
divisor = 1
while divisor <= n:
    if n % divisor == 0:
        print(divisor)
    divisor += 1