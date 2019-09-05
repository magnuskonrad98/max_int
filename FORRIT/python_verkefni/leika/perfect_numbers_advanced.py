highest_int = int(input("Enter highest integer in range: "))

x = 1
while x <= highest_int:
    divisor = 1
    sum_of_divisors = 0
    while divisor < x:
        if x % divisor == 0:
            sum_of_divisors += divisor
        
        divisor += 1
    if sum_of_divisors == x:
        print(x)
    x += 1

print("Done!")



