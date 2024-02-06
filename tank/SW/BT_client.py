# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:45:08 2024

@author: clive
"""

import pickle
import bluetooth
from BT_base_class import BT_base

class BT_client(BT_base):
    def __init__(self, port, server_address="DC:A6:32:9C:1C:F5", rx_data_size_inBytes=1024):
        self.rx_data_size_inBytes = rx_data_size_inBytes
        super().__init__(port, server_address)
        
        
if __name__ == "__main__":
    import time
    from mapping import dict_buttonMapping
    
    port = 1
    obj_client = BT_client(port)
    
    try:    
        while True:
            dict_controllerStatus = obj_client.listen()
            
            if not(dict_controllerStatus is None):
                print("\n===========================================\n")
                print(f"\tA_BUTTON     = {dict_controllerStatus['A_BUTTON']}\n")
                print(f"\tB_BUTTON     = {dict_controllerStatus['B_BUTTON']}\n")
                print(f"\tX_BUTTON     = {dict_controllerStatus['X_BUTTON']}\n")
                print(f"\tY_BUTTON     = {dict_controllerStatus['Y_BUTTON']}\n")
                print(f"\tL_BUMPER     = {dict_controllerStatus['L_BUMPER']}\n")
                print(f"\tR_BUMPER     = {dict_controllerStatus['R_BUMPER']}\n")
                print(f"\tBACK_BUTTON  = {dict_controllerStatus['BACK_BUTTON']}\n")
                print(f"\tSTART_BUTTON = {dict_controllerStatus['START_BUTTON']}\n")
                print(f"\tL_TRIGGER    = {dict_controllerStatus['L_TRIGGER']}\n")
                print(f"\tR_TRIGGER    = {dict_controllerStatus['R_TRIGGER']}\n")
                print(f"\t{dict_buttonMapping['L_JOYSTICK_X']} = {dict_controllerStatus[dict_buttonMapping['L_JOYSTICK_X']]}\n")
                print(f"\t{dict_buttonMapping['L_JOYSTICK_Y']} = {dict_controllerStatus[dict_buttonMapping['L_JOYSTICK_Y']]}\n")
                print(f"\tR_JOYSTICK_X = {dict_controllerStatus['R_JOYSTICK_X']}\n")
                print(f"\tR_JOYSTICK_Y = {dict_controllerStatus['R_JOYSTICK_Y']}\n")
                print(f"\tL_JOYSTICK_BUTTON = {dict_controllerStatus['L_JOYSTICK_BUTTON']}\n")
                print(f"\tR_JOYSTICK_BUTTON = {dict_controllerStatus['R_JOYSTICK_BUTTON']}\n")
                
                print("\n\n")
                time.sleep(1)  # Adjust delay as needed
            else:
                break
        obj_client.killInstance()
        
    except KeyboardInterrupt:
        print("Client terminated by user.")
    
    finally:
        obj_client.killInstance()
        
