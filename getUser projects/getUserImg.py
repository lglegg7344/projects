import picamera, time

def getPicture(name):
    try:
        with picamera.PiCamera() as camera:
            check = False
            while check == False:
                imgname = input ("what is your name?")
                camera.start_preview()

                time.sleep(2)

                camera.capture("{0}.jpeg".format(imgname))
                camera.stop_preview()

                pic = input ("Are you happy with this image?")
                if pic.lower() == "y":
                    check = True

    except picamera.exc.PiCameraMMALError:
        print("your camera has not been detected. Please plug your camera in and restart.")
        imgname=""

        
