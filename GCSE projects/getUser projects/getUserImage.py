#This file contains all the functions required for guess who

import picamera, time

#Gets a picture of the user

def getUserImage():

    check = False
    while check == False:

        with picamera.PiCamera() as camera:
            camera.resolution = (1024,768)

            imgname = input ("what do you want your photo to be called?")
            camera.start_preview()

            time.sleep(2)
        
            camera.capture("{0}.jpg".format(imgname))
            camera.stop_preview()

            pic = input("Are you happy with this picture?")
            if pic.lower() == "y":
                check = True

    
        
        
        
        
    
