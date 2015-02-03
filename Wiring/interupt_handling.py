#!/usr/bin/python
import RPi.GPIO as GPIO #imports RPi.GPIO, calling it GPIO

pin = 27 #sets pin 27 to pin
count = 0

def bucket_tipped(channel):
    global count
    count += 1
    print (count *0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

input("Press enter to start...")
