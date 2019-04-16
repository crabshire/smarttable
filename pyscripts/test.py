#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
import time
import RPi.GPIO as GPIO
import pigpio

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(17, False)
    lighton = False
    pi = pigpio.pi()
    pi.set_PWM_dutycycle(5, 128)
    pi.set_PWM_dutycycle(6, 128)
    pi.set_PWM_dutycycle(13, 128)
    pi.stop()
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
