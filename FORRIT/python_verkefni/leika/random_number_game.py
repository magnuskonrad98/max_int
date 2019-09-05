import random
number = random.randint(0, 100)
print("This is a game where you guess a random number between 0 and 100")
my_int = int(input("Guess the number: "))

while 0 <= my_int <= 100:
    if my_int == number:
        print("Thats right!")
        break
    elif my_int < number:
        print("Try higher!")
    else:
        print("Try lower!")
    my_int = int(input("Guess the number: "))
else:
    print("Why did you quit? :'(")