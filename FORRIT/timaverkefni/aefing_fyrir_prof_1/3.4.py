#Write a program using a while statement, 
#that given an int as the input, prints all the factors of that number, one in each line.
#For example, if the input is


number_ = int(input("Enter: "))
count = 1
while count <= number_:
    if number_ % count == 0:
        print(count)
    count += 1