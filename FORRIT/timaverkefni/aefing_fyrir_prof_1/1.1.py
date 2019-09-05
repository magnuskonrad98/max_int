#Einstein's famous equation states that the energy 
# in an object at rest equals its mass times the 
# square of the speed of light.  (The speed of light is 300,000,000 m/s.)

#Complete the skeleton code below so that it:
# Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
#* Calculate the energy, e
#* Prints e

mass_float = float(input("Enter mass: "))
energy_float = mass_float * ((300000000)**(2))
print(energy_float)