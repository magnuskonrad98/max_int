m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

gdc = 0

for i in range(1, m):
    if m % i == 0 and n % i == 0:
        if i > gdc:
            gdc = i
print(gdc)

