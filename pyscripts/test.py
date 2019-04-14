#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
import time
import RPi.GPIO as GPIO

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.output(18, False)
    lighton = False
    while True:
        if GPIO.input(23):
            if lighton == True:
                GPIO.output(18, False)
                lighton = False
                time.sleep(1)
            else:
                GPIO.output(18, True)
                lighton = True
                time.sleep(1)
        if GPIO.input(24):
            exit()
if __name__ == "__main__":
    main()
