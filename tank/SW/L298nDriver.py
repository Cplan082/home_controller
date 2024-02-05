# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:18:17 2024

@author: clive
"""

import pigpio
from pi_hw_pwm_drv import piHwPwmDriver

class L298nDriver:
    def __init__(self, pi, dict_pin_in, freq, invert_a=False, invert_b=False):
        # Initialize the L298nDriver class with necessary parameters
        self.pi = pi
        self.pwmDrv_a = piHwPwmDriver(self.pi, '0', freq)
        self.pwmDrv_b = piHwPwmDriver(self.pi, '1', freq)
        self.dict_pin_in = dict_pin_in
        
        # Variables to store the old directions of motors
        self.old_direction_a = 0
        self.old_direction_b = 0
        
        # Check if inversion is needed for motor directions
        if invert_a:
            self.inverter_a = -1
        else:
            self.inverter_a = 1
            
        if invert_b:
            self.inverter_b = -1
        else:
            self.inverter_b = 1
        
        # Configure GPIO pins as outputs
        for value in dict_pin_in.values():
            print(f"value = {value}\n")
            self.pi.set_mode(value, pigpio.OUTPUT)
    
    def drive_motors(self, vector_a, vector_b):
        # # Calculate vectors for each motor based on input parameters
        # vector_a = y + x
        # vector_b = y - x
        
        # Update motor directions
        self.update_direction(vector_a, vector_b)

        # Limit the magnitude of vectors to 1 and set PWM duty cycles
        magnitude_a = min(abs(vector_a), 1)
        magnitude_b = min(abs(vector_b), 1)
        
        self.pwmDrv_a.setDuty(magnitude_a)
        self.pwmDrv_b.setDuty(magnitude_b)
    
    def update_direction(self, vector_a, vector_b):
        # Determine the direction of each motor based on the vectors
        if vector_a > 0:
            new_direction_a = 1
        else:
            new_direction_a = -1
        
        if vector_b > 0:
            new_direction_b = 1
        else:
            new_direction_b = -1
        
        # Apply inversion if needed
        new_direction_a = int(new_direction_a * self.inverter_a)
        new_direction_b = int(new_direction_b * self.inverter_b)
        
        # Change direction if there's a change
        if new_direction_a != self.old_direction_a:
            self.old_direction_a = new_direction_a
            self.change_direction(new_direction_a, 'in1', 'in2')
            
        if new_direction_b != self.old_direction_b:
            self.old_direction_b = new_direction_b
            self.change_direction(new_direction_b, 'in3', 'in4')
            
    def change_direction(self, new_direction, key1, key2):
        # Change the direction of the motor by setting GPIO pins
        if new_direction > 0:
            self.pi.write(self.dict_pin_in[key1], 1)
            self.pi.write(self.dict_pin_in[key2], 0)
        else:
            self.pi.write(self.dict_pin_in[key1], 0)
            self.pi.write(self.dict_pin_in[key2], 1)
        
        
    def shutdown_motors(self):
        # Stop PWM for both motors to shut down the motors
        self.pwmDrv_a.stopPwm()
        self.pwmDrv_b.stopPwm()
        
        
if __name__ == "__main__":
    pass
    # dict_pin_in = {"in1": ,
    #                "in2": ,
    #                "in3": ,
    #                "in4": }
