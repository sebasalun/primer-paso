led.py
#Led para raspberry en python

import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while:
	GPIO.output(4, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(4, GPIO.LOW)
	time.sleep(2)
return
