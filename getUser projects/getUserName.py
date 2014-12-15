def getUserName(): #defines getUserName()
    check = False
    while check == False:
        name = input("What is your name?") #asks for user's name
        correct = input ("Confirm that your name is {0} by pressing y, or crrect your name by pressing n".format(name)) #you could also say -print("Your name is" + name)-
        #if the user presses y, check is true
        if correct.lower() == "y":
            check = True
