x=10

while x < 100:
    a = x ** 2
    if a % 100 == x:
        print(x)
        break
    else:
        x += 1