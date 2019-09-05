n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
divisor = 2
while divisor < n:
    if n % divisor == 0:
        prime = False
        break
    else:
        divisor += 1
else:
    prime = True


# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")