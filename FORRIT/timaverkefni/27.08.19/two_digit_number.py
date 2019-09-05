a = 10
while a < 100:
    b = a ** 2
    if b % 100 == a:
        break
    a += 1
print(b)
