

a = int(input("Enter a num: "))
b = int(input("Enter a num: "))

for x in range (1, a):
    if a % x == 0 and b % x == 0:
        gcd = x

print(gcd)