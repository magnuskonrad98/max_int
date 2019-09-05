number = int(input("Enter an integer: "))

sum_of_divisors = 0

for x in range(1, number + 1):
    if number % x == 0:
        sum_of_divisors += x

sum_of_divisors -= number

if sum_of_divisors == number:
    print("The number is perfect!")
elif sum_of_divisors > number:
    print("The number is abundant!")
else:
    print("The number is deficient!")