import RPi.GPIO as GP,time #imports time, and RPi.GPIO and calling it GP
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

GP.output(11,GP.HIGH) #turns light on
time.sleep(0.5) #pauses for 1/2 a second
GP.output(11,GP.LOW) #turns light off
time.sleep(0.25) #pauses for 1/4 of a second
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.75) #pauses for 3/4 of a second

GP.output(11,GP.HIGH)
time.sleep(1) #pauses for a second
GP.output(11,GP.LOW)
time.sleep(0.25) 
GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(1)
GP.output(11,GP.LOW)
time.sleep(0.75)

GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.25)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(1) #pauses for 1 second
