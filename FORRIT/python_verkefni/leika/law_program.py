name = input("Enter your name: ")

act = input("Is it legal to commit a/an: ")

illegal = ["murder", "robbery", "armed robbery", "assault", "theft", "blackmail"]
legal = ["sing a song"]

if act in illegal:
    print("Dear ", name, "it is NOT legal to commit a ", act, ", though it might be cool!")

elif act in legal:
    print("Dear ", name, "it IS legal to commit a ", act, ", and you should go ahead and do it!")

else:
    print("Dear ", name, ", I have no idea if it is legal to commit a ", act, ", or not, but you should just try and see what happens!")


