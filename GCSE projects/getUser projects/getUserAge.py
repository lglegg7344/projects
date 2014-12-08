def getUserAge():
    check = False
    while check == False:
        age = input ("How old are you")
        correct = input ("Confirm that you are {0} years of age by pressing y, or press n to correct your age".format(age))
        if correct.lower() == "y":
            check = True
        
