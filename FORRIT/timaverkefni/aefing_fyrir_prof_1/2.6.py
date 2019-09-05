#Accept d1 and d2, the number on two dices as input. 
# First, check to see that they are in the proper range for dice (1-6). 
# If not, print the message "Invalid input". 
# Otherwise, determine the sum. If the sum is 7 or 11, print "Winner". 
# If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.

dice_1 = int(input("Enter dice 1: "))
dice_2 = int(input("Enter dice 2: "))

if 1 <= dice_1 <= 6 and 1 <= dice_2 <= 6:
    sum_of = dice_1 + dice_2
    if sum_of == 7 or sum_of == 11:
        print("Winner")
    elif sum_of == 2 or sum_of ==3 or sum_of == 12:
        print("Loser")
    else:
        print(sum_of)
else:
    print("Invalid input!!!!!")