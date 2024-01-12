# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:11:49 2024

@author: clive
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 1000)  # Pin 18, frequency 1000 Hz

pwm.start(50)  # 50% duty cycle

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()