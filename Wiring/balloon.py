import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 24
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
print ("Ready...")
GPIO.wait_for_edge(button, GPIO.FALLING)
print("Pop!")
