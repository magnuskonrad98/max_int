

my_int = int(input("Enter a 6 number number lol: "))
first_three = my_int // 1000
middle_two = my_int % 10000
middle_two = middle_two // 100
last_two = my_int % 100

print(first_three)
print(middle_two)
print(last_two)