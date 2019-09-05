years = int(input("Years: "))

seconds = 365.0 * 24.0 * 60.0 * 60.0
births = seconds / 7.0
deaths = seconds / 13.0
immigrants = seconds / 35.0

new_people = years * (births + immigrants - deaths)

population = 307357870.0

if years < 0:
    print("Invalid input!")
else:
    population += new_people
    print("New population after", years, "years is", int(population))
