#This file contains all the functions required for guess who

import picamera, time #imports picamera and time

#Gets a picture of the user

def getUserImage(): #defines getUserImage()

    check = False
    while check == False: #if check is false, the code will restart

        with picamera.PiCamera() as camera: #gets picamera.Picamera and calls it camera 
            camera.resolution = (1024,768) #sets the picture resolution

            imgname = input ("what do you want your photo to be called?") #asks what the user wants the image to be called
            camera.start_preview() #starts the preview

            time.sleep(2) #pauses for 2 seconds
        
            camera.capture("{0}.jpg".format(imgname)) #saves as the name the user gave and adds .jpg at the end
            camera.stop_preview() #stops the preview

            pic = input("Are you happy with this picture?") #asks for confirmation
            
            #if the user presses y, check is true
            if pic.lower() == "y": 
                check = True
