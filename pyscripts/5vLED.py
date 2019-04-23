#!/usr/bin/env python
"""test.py, by Chris
This program is my first python test program
"""
from rpi-ws281x import *
import time
import RPi.GPIO as GPIO
import pigpio
import os
import threading

#Global Variable Setup
global lighton
global ledrun
global total_LED_count
global brightness
global frequency
global DMA
global pin

lighton = False
ledrun = False
total_LED_count = 40
brightness = 128 #0-255
frequency = 800000 #should stay at 800k
DMA = 10 #try 10 if 5 doesn't work
pin = 18 #18 is the PWM pin

def led2_child():
    strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
    strip.show()

def led_child():
    pi = pigpio.pi()
    pi.set_PWM_dutycycle(5, 0)
    pi.set_PWM_dutycycle(6, 0)
    pi.set_PWM_dutycycle(13, 0)
    time.sleep(.25)
    pi.set_PWM_dutycycle(5, 128)
    pi.set_PWM_dutycycle(6, 128)
    pi.set_PWM_dutycycle(13, 128)
    time.sleep(.25)
    pi.set_PWM_dutycycle(5, 255)
    pi.set_PWM_dutycycle(6, 255)
    pi.set_PWM_dutycycle(13, 255)
    time.sleep(.5)
    pi.set_PWM_dutycycle(5, 0)
    pi.set_PWM_dutycycle(6, 0)
    pi.set_PWM_dutycycle(13, 0)
    time.sleep(.5)
    while ledrun:
        for x in range(255):
            pi.set_PWM_dutycycle(5, x)
            time.sleep(.05)
            for y in range(255):
                pi.set_PWM_dutycycle(6, y)
                time.sleep(.05)
                for z in range(255):
                    pi.set_PWM_dutycycle(13, z)
                    time.sleep(.05)
    pi.set_PWM_dutycycle(5, 0)
    pi.set_PWM_dutycycle(6, 0)
    pi.set_PWM_dutycycle(13, 0)
    pi.stop()

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    #led_thread = threading.Thread(target=led_child)
    strip = Adafruit_NeoPixel(total_LED_count, pin, frequency, DMA, False, brightness)
    strip.begin()
    R = 0
    G = 0
    B = 0
    while True:
        for R in range(0, 128, 16):
            strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
            for G in range(0, 128, 16):
                strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
                for B in range (0, 128, 16):
                    strip.setPixelColorRGB(LED_CHIP_NUMBER, R, G, B)
        if GPIO.input(22):
            exit()
if __name__ == "__main__":
    main()
