# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:18:01 2024

@author: clive
"""

import pigpio
import time

pi = pigpio.pi()

if not pi.connected:
    exit()

gpio_pin = 18  # Replace with the GPIO pin you want to use
frequency = 1000  # Set the PWM frequency in Hz
duty_cycle = 500000  # Set the PWM duty cycle (0 to 1000000)

pi.hardware_PWM(gpio_pin, frequency, duty_cycle)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pi.set_mode(gpio_pin, pigpio.INPUT)  # Set the GPIO pin back to INPUT mode
    pi.stop()