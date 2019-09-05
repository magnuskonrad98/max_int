top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1, top_num + 1):
    sum_of_divisors = 0
    for x in range(1, i):
        if i % x == 0:
            sum_of_divisors += x
    if sum_of_divisors == i:
        print(i)
