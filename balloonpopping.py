import picamera,time

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.framerate = 90
    camera.start_recording('balloon-popping.h264')
    camera.start_preview()
    camera.wait_recording(60)
    camera.stop_preview()
    camera.stop_recording()
  
    
    
                           
