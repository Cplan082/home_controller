# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:00:39 2024

@author: clive
"""
import pigpio
from ..common_functions import common as cm

class servoDriver:
    def __init__(self, 
                 Smallest_pw, 
                 largest_pw, 
                 pin_pwm, 
                 old_low_rng=-90, 
                 old_high_rng=90,
                 freq=50):
        
        self.Smallest_pw = Smallest_pw
        self.largest_pw = largest_pw
        self.freq = freq
        self.pin_pwm = pin_pwm
        self.old_low_rng = old_low_rng
        self.old_high_rng = old_high_rng
        
        self.pi = pigpio.pi()
        if not self.pi.connected:
            exit() 
            
        self.pi.set_mode(pin_pwm, pigpio.OUTPUT)
        
        
    def getDuty(self,angle):
        T_on = cm.map_value(angle, 
                         self.old_low_rng, 
                         self.old_high_rng, 
                         self.Smallest_pw, 
                         self.largest_pw)
        
        # Ensure the duty cycle is within the valid range [0, 1000000]
        duty_cycle = int(min(max(T_on * self.freq * 1e6, 0), 1000000))
        
        return duty_cycle
        
        
        
    def driveServo(self, angle):
        duty_cycle = self.getDuty(angle)
        self.pi.hardware_PWM(self.pin_pwm, self.freq, duty_cycle)

        
    def killInstance(self):
        self.pi.hardware_PWM(self.pin_pwm, 0, 0)  # Stop PWM
        self.pi.stop()
        
    
if __name__ == "__main__":
    Smallest_pw = 1e-3
    largest_pw = 2e-3
    pin_pwm = 18
    obj = servoDriver(Smallest_pw, largest_pw, pin_pwm)
    
    try:
        while True:
            angle = int(input("Set angle to: "))
            
            if angle > 90:
                angle = 90
            elif angle < -90:
                angle = -90
                
            print("\n")
            obj.driveServo(angle)
            
    except KeyboardInterrupt:
        print("Client terminated by user.")
        
    finally:
        obj.killInstance()