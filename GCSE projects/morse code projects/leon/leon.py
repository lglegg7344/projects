import RPi.GPIO as GP,time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)


GP.output(11,GP.HIGH)
time.sleep(0.25)
GP.output(11,GP.LOW)
time.sleep(0.5)
GP.output(11,GP.HIGH)
time.sleep(0.75)
GP.output(11,GP.LOW)
time.sleep(0.5)
GP.output(11,GP.HIGH)
time.sleep(0.25)
GP.output(11,GP.LOW)
time.sleep(0.5)
GP.output(11,GP.HIGH)
time.sleep(0.25)
GP.output(11,GP.LOW)
time.sleep(1)


GP.output(11,GP.HIGH)
time.sleep(0.25)
GP.output(11,GP.LOW)
time.sleep(1)


GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.75)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.75)
GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(1)

GP.output(11,GP.HIGH)
time.sleep(0.5)
GP.output(11,GP.LOW)
time.sleep(0.75)
GP.output(11,GP.HIGH)
time.sleep(0.25)
GP.output(11,GP.LOW)
time.sleep(0.75)


