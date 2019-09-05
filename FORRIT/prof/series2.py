first_int = int(input("First: "))
step_int = int(input("Step: "))

sum_of_series = 0

for x in range(first_int, 101, step_int):
    sum_of_series += x
    print(x, end=' ')
    if sum_of_series > 100:
        break

print()
print("Sum of series: ", sum_of_series)