# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:51:38 2024

@author: clive
"""
import pigpio

import BT_client as btc
from L298nDriver import L298nDriver
from mapping import dict_buttonMapping

port = 1
motor_freq = 50
dict_pin_in = {'in1': 23,
               'in2': 24,
               'in3': 6,
               'in4': 26,
               }

obj_client = btc.client_BT(port)

pi = pigpio.pi()
if not pi.connected:
    exit()  # Exit if connection to pigpio daemon fails
    
obj_L298nDriver = L298nDriver(pi, dict_pin_in, motor_freq, invert_a=False, invert_b=False)

try:
    while True:
        dict_controllerStatus = obj_client.listen()
        
        xAxis_tank = dict_controllerStatus["TANK_CNTRL_X"]
        yAxis_tank = dict_controllerStatus["TANK_CNTRL_Y"]
        
        vector_a = yAxis_tank + xAxis_tank
        vector_b = yAxis_tank - xAxis_tank
        
        obj_L298nDriver.drive_motors(vector_a, vector_b)
        

    obj_client.killInstance()
    
except KeyboardInterrupt:
    print("Tank Controller terminated by user.")

finally:
    obj_client.killInstance()
    obj_L298nDriver.shutdown_motors()
