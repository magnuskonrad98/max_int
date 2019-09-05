size = int(input("Enter the degree of the equation: "))

my_equation = int(0)


for number in range(size):
    a = int(input("Enter a: "))
    my_equation += a * x ** size
    size -= 1

print("Your equation is: ", my_equation, "=0")

