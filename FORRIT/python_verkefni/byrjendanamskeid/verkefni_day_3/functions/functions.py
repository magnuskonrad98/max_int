def sum_of_two(x, y):
    result = x + y
    return result

def difference(halli, laddi):
    result = halli - laddi
    return result

def product_of_two(x, y):
    result = x * y
    return result

def quotient(x, y):
    result = x / y
    return result

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c = sum_of_two(a, b)
print(c)

d = difference(a, b)
print(d)

e = product_of_two(a, b)
print(e)

f = quotient(a, b)
print(f)
