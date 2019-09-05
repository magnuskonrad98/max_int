#BMI is a number calculated from a person's weight and height.  The formula for BMI is:
#weight / height2
#where weight is in kilograms and heights is in meters
#Write a program  that prompts for weight in kilograms and height in centimeters and outputs the BMI.

weight_fl = float(input("Enter weight in kgs: "))
height_fl = float(input("Enter height in cms: "))

height_fl /= 100

bmi = weight_fl / (height_fl ** 2)
print (bmi)
