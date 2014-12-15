#outputs Leon in morse code

import RPi.GPIO as GP #imports RPi.GPIO and calls it GP
import time #imports time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)
    

GP.output(11,GP.HIGH) #turns LED on
time.sleep(0.25) #pauses for .25 of a second
GP.ouyput(11,GP.LOW) #turns LED off
time.sleep(025)
GP.output(11,GP.HIGH)
time.sleep(1) #pauses for 1 second
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH) 
time.sleep(0.25)
GP.ouyput(11,GP.LOW)
time.sleep(025) 
GP.output(11,GP.HIGH) 
time.sleep(0.25)
GP.ouyput(11,GP.LOW)
time.sleep(025) 


GP.output(11,GP.HIGH) 
time.sleep(0.25)
GP.ouyput(11,GP.LOW)
time.sleep(025) 


GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.25)

GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
