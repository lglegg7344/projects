import picamera, time #imports picamera and time

with picamera.PiCamera() as camera: #using picamera.PiCamera(), but called camera, ....
    camera.resolution = (1024,768) #sets resolution
    camera.start_preview() #starts preview

    time.sleep(2) #pauses for 2s
    camera.capture("picam-capture.jpeg") #takes the pic and saves it
