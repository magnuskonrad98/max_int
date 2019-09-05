#A prime number is a whole number greater than 1 whose only factors are 1 and itself.

#Write a program using a while statement, that given an int as the input, prints out 
#"Prime" if the int is a prime number, otherwise it prints "Not prime".

number1 = int(input("enter number:"))
count = 2
while count < number1:
    if number1 % count == 0:
        prime = False
        break
    else:
        count += 1
else:
    prime = True

print(prime)
