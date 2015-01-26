import time
import picamera

def getUserProfile():

    #photo 

    check = False
    while check == False:
        with picamera.PiCamera() as camera:
            filename = input ("what is your name?")
            camera.start_preview()

            time.sleep(1)

            camera.capture("[0].jpg".format(filename))
            camera.stop_preview()

            pic = input ("are you happy with this picture?")
            if pic.lower() == "y":
                check = True
            
    #name
                
    check = False
    while check == False:
        name = input ("what is your first name?")
        correct = input ("is your name {0}?".format(name))
        if correct == "y":
            check = True
            print ("your name has been set as {0}.".format(name))
    check = False

    #hair colour

    hair = ""
    while not (hair in ["black","ginger","brown","blonde"]):
        hair = input ("what colour is your hair?") 

    #eye colour

    eyes = ""
    while not (eyes in ["blue","brown","green"]):
        eyes = input ("what colour are your eyes?")

    #gender

    gender = ""
    while not (gender in ["male","female"]):
        gender = input ("are you male or female?")
