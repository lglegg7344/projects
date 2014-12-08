import time
import picamera

def getUserProfile():

    #photo 

    check = False
    while check == False:
        withpicamera.PiCamera as camera:
            camera.resolution = (1024, 768)
            filename = input ("what is your name?")
            camera.start_preview()

            time.sleep(2)

            camera.capture("[0].jpg".format(filename))
            camera.stop_preview()

            pic = input ("are you happy with this picture?")
            if pic.lower() == "y":
                check = True
            
    #name
    check = False
    while check == False:
        name = input ("what is your first name?")
        correct = input ("is your first name {0}?".format(fname))
        if correct == "y":
            check = True
            print ("your first name has been set as {0}.".format(fname))
    check = False

    #hair colour

    hair = ""
    while not (hair in ["black","ginger","brown","blonde"]):
        hair = input ("what colour is your hair?")
        
    
