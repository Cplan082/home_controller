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
dict_pin_in = {'in1': 25,
               'in2': 8,
               'in3': 7,
               'in4': 1,
               }

obj_client = btc.client_BT(port)

pi = pigpio.pi()
if not pi.connected:
    exit()  # Exit if connection to pigpio daemon fails
    
obj_L298nDriver = L298nDriver(pi, dict_pin_in, motor_freq)

try:
    while True:
        dict_controllerStatus = obj_client.listen()
        
        xAxis_tank = dict_controllerStatus["TANK_CNTRL_X"]
        yAxis_tank = dict_controllerStatus["TANK_CNTRL_Y"]
        
        vector_a = yAxis_tank + xAxis_tank
        vector_b = yAxis_tank - xAxis_tank
        
        obj_L298nDriver(vector_a, vector_b)
        

    obj_client.killInstance()
    
except KeyboardInterrupt:
    print("Tank Controller terminated by user.")

finally:
    obj_client.killInstance()