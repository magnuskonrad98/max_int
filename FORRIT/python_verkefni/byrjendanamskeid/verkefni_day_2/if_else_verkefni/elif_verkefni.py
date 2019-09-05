days_since_pizza = int(input("How many days since your last pizzza? "))
your_diner = ""

if days_since_pizza > 7:
    your_diner = "pizza in acqui"

elif days_since_pizza <= 7 and days_since_pizza > 5:
    your_diner = "flatey"

else:
    your_diner = "dominos"

print(("Your diner tonight will be: "), your_diner)
