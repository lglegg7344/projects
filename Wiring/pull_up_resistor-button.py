#!/usr/bin/python
import RPi.GPIO as GPIO #imports RPi.GPIO, calling it GPIO
import time #imports time

pin = 27 #sets pin 27 to pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

while True: #infinite loop
    pin_value = GPIO.input(pin)
    print ("HIGH" if pin_value else "LOW")
    time.sleep(0.01) #how fast the button reacts
