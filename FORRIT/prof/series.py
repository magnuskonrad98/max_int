first_int = int(input("First: "))
step_int = int(input("Step: "))

sum_of_series = 0
number_int = first_int
print(number_int, end=' ')
sum_of_series += number_int

while sum_of_series < 100:
    number_int += step_int
    print(number_int, end=' ')
    sum_of_series += number_int

print()
print("Sum of series: ", sum_of_series)

