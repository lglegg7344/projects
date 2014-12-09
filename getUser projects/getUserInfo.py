import time
import picamera

#This code will get all the user info needed for a small profile (like a small survey) but will not store the info quite yet

def getUserInfo():
    #name
    check = False
    while check == False:
        name = input ("What is your name?")
        correct = input ("confirm that your name is {0} by pressing y, or correct it by pressing n.".format(name))
        if correct.lower() == "y":
            check = True
            print ("your name has been set as {0}.".format(name))

    time.sleep(1)

    #surname
    check = False
    while check == False:
        surname = input ("what is your surname?")
        correct = input ("confirm that your surname is {0} by pressing y, or press n to correct.".format(surname))
        if correct.lower() == "y":
            check = True
            print ("your surname has been set as {0}.".format(surname))
             
    
    time.sleep(1)

    #age
    check = False
    while check == False:
        age = input("How old are you?")
        correct = input ("confirm that you are {0} years of age by pressing y, or press n to correct.".format(age))
        if correct.lower() == "y":
            check = True
            print ("your age has been set as {0} years old.".format(age))

    time.sleep(1)

    #D.O.B
    check = False
    while check == False:
        DOB = input ("What is your date of birth?")
        correct = input ("Confirm that your date of birth is {0} by pressing y, or press n to correct.".format(DOB))
        if correct.lower() == "y":
            check = True
            print ("your Date of birth has been set as {0}.".format(DOB))

    time.sleep(1)

    check = False
    while check == False:

        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            imgname = input ("what do you want your photo's name to be?")
            camera.start_preview()

            time.sleep(2)
            
            camera.capture("{0}.jpeg".format(imgname))
            camera.stop_preview()

            pic = input ("are you happy with your picture?")
            if pic.lower() == "y":
                check = True
                print ("your image has been saved as {0}.jpg".format(imgname))
    
        
    
