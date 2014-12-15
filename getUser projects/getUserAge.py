def getUserAge(): #defines getUserAge()
    check = False #check is false
    while check == False: #if check is false, the code will start again
        age = input ("How old are you") #asks how old you are
        correct = input ("Confirm that you are {0} years of age by pressing y, or press n to correct your age".format(age)) #asks for confirmation
    #if user presses y, check is true. If any other button is pressed, it is false, so it will start again.
        if correct.lower() == "y": 
            check = True #check is true
