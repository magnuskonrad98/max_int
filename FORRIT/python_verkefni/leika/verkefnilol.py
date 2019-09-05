print("For equation: ax^2 + bx + c = 0: ")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b**2 - 4*a*c

if (d < 0):
    print("The equation has no solution")

elif (d == 0):
    x = -b / 2*a
    print("The equation has one solution: x = ", x)

else:
    x = (-b + d**(1/2)) / 2*a
    y = (-b - d**(1/2)) / 2*a
    print("The equation has two solutions: x = ", x, "or: x = ", y)

    