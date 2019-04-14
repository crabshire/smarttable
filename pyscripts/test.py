#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
import time
import RPi.GPIO as GPIO

def main():
    loopcontrol = False   # flag variable to see if they guessed it
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.IN)

while not loopcontrol:
        #GPIO.output(18, True)
        #time.sleep(2)
        #GPIO.output(18, False)
        #time.sleep(1)
	pressed = GPIO.input(23)
	lighton = False
	if pressed == True:
		if lighton == True:
			GPIO.output(18, False)
			lighton = False
			pressed = False
		else:
			GPIO.output(18, True)
			lighton = True
			pressed = False


if __name__ == "__main__":
    main()
