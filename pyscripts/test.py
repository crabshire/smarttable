#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
import time
import RPi.GPIO as GPIO

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.output(17, False)
    lighton = False
    while True:
        if GPIO.input(27):
            if lighton == True:
                GPIO.output(17, False)
                lighton = False
                time.sleep(1)
            else:
                GPIO.output(17, True)
                lighton = True
                time.sleep(1)
        if GPIO.input(22):
            exit()
if __name__ == "__main__":
    main()
