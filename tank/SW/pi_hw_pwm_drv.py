# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:40:18 2024

@author: clive
"""

import pigpio
# from ...packages.common_functions import common as cm
import common as cm

class piHwPwmDriver:
    dict_pwmPins = {"0": [18, 12],
                    "1": [19, 13]}
    def __init__(self, pi, pwm_no, freq):
        self.pin = piHwPwmDriver.dict_pwmPins[pwm_no][0]
        self.pwm_no = int(pwm_no)
        print(f"initalizing PWM{self.pwm_no} on pin {self.pin}\n\n")
        # Connect to pigpio daemon
        self.pi = pi
        self.pi.set_mode(self.pin, pigpio.OUTPUT)
        self.freq = freq
        
        
    def setDuty(self, duty_cycle):
        self.pi.hardware_PWM(self.pin, self.freq, int(duty_cycle*1e6))
    
    def killInstance(self):
        """
        Stop PWM and disconnect from pigpio daemon.
        """
        print(f'Killing PWM{self.pwm_no}\n')
        self.pi.hardware_PWM(self.pin, 0, 0)  # Stop PWM
        print(f'PWM{self.pwm_no} has been killed\n\n')
        

if __name__ == "__main__":
    import time
    pi = pigpio.pi()
    if not pi.connected:
        exit()  # Exit if connection to pigpio daemon fails
        
    freq = 50
    obj_pwm0 =  piHwPwmDriver(pi, '0', freq)
    obj_pwm1 =  piHwPwmDriver(pi, '1', freq)
    
    try:
        duty0 = 0
        duty1 = 0.5
        while True:
            duty0 += 0.1
            duty1 += 0.1
            
            if duty0 > 1:
                duty0 = 0
                
            if duty1 > 1:
                duty1 = 0
                
            obj_pwm0.setDuty(duty0)
            obj_pwm1.setDuty(duty1)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("PWMs terminated by user.")
        
    finally:
        # Stop PWM and disconnect from pigpio daemon
        obj_pwm0.killInstance()
        obj_pwm1.killInstance()
        pi.stop()
