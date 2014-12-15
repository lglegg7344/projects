import time #imports time
import picamera #imports picamera

#This code will get all the user info needed for a small profile (like a small survey) but will not store the info quite yet

def getUserInfo(): #defines getUserInfo()
    #name
    check = False
    while check == False:
        name = input ("What is your name?") #asks for user's name
        correct = input ("confirm that your name is {0} by pressing y, or correct it by pressing n.".format(name)) #asks for user's confimation
        #if the user presses y, check is true
        if correct.lower() == "y":
            check = True
            print ("your name has been set as {0}.".format(name)) #says "your name has been set as 'your name'"

    time.sleep(1) #pauses for 1 second

    #surname
    check = False
    while check == False:
        surname = input ("what is your surname?") #asks user for theis surname
        correct = input ("confirm that your surname is {0} by pressing y, or press n to correct.".format(surname)) #asks for user's confirmation
        #if the user presses  y, check is true
        if correct.lower() == "y":
            check = True
            print ("your surname has been set as {0}.".format(surname)) #says "your surname has been set as 'your surname'"
             
    
    time.sleep(1) #pauses for 1 second

    #age
    check = False
    while check == False:
        age = input("How old are you?") #asks for user's age
        correct = input ("confirm that you are {0} years of age by pressing y, or press n to correct.".format(age)) #asks for user's confirmation
        #if user presses y, check is true
        if correct.lower() == "y":
            check = True
            print ("your age has been set as {0} years old.".format(age)) #says "your age has been set as 'your age' years old"

    time.sleep(1) #pauses for 1 second

    #D.O.B
    check = False
    while check == False:
        DOB = input ("What is your date of birth?") #asks for user's date of birth
        correct = input ("Confirm that your date of birth is {0} by pressing y, or press n to correct.".format(DOB)) #asks for user's confirmation
        #if user presses y, check is true
        if correct.lower() == "y":
            check = True
            print ("your Date of birth has been set as {0}.".format(DOB)) #says "your date of birth has beens set as 'your date of birth'"

    time.sleep(1)

    check = False
    while check == False:

        with picamera.PiCamera() as camera: #give picamera.PiCamera() the name camera and then....
            camera.resolution = (1024, 768) #set's the resolution
            imgname = input ("what do you want your photo's name to be?") #asks for a name for the image
            camera.start_preview() #starts the preview

            time.sleep(2) #pauses for 2 seconds
            
            camera.capture("{0}.jpeg".format(imgname)) #takes the picture and calls it 'the name given'.jpg
            camera.stop_preview() #stops preview

            pic = input ("are you happy with your picture?") #asks for confirmation
            #if user presses y, check is true
            if pic.lower() == "y":
                check = True
                print ("your image has been saved as {0}.jpg".format(imgname)) #says "your image has been set as 'name given'jpg"
