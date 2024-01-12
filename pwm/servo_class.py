# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:00:39 2024

@author: clive
"""
import pigpio

class servoDriver:
    def __init__(self, Smallest_pw, largest_pw, pin_pwm, freq=50):
        self.Smallest_pw = Smallest_pw
        self.largest_pw = largest_pw
        self.freq = freq
        self.pin_pwm = pin_pwm
        
        self.pi = pigpio.pi()
        if not self.pi.connected:
            exit() 
            
        self.pi.set_mode(pin_pwm, pigpio.OUTPUT)
        
        
    def driveServo(self, angle):
        T_on = map_value(angle, -90, 90, self.Smallest_pw, self.largest_pw)
        
        # Ensure the duty cycle is within the valid range [0, 1000000]
        duty_cycle = int(min(max(T_on * self.freq * 1e6, 0), 1000000))
        
        self.pi.hardware_PWM(self.pin_pwm, self.freq, duty_cycle)

        
    def killInstance(self):
        self.pi.hardware_PWM(self.pin_pwm, 0, 0)  # Stop PWM
        self.pi.stop()
        

def map_value(value, old_min, old_max, new_min, new_max):
    """
    Map a value from one range to another using linear mapping.

    Parameters:
    - value: The original value to be mapped.
    - old_min: The minimum value of the original range.
    - old_max: The maximum value of the original range.
    - new_min: The minimum value of the desired range.
    - new_max: The maximum value of the desired range.

    Returns:
    The mapped value in the new range.
    """
    old_range = old_max - old_min
    new_range = new_max - new_min

    # Perform linear mapping
    new_value = ((value - old_min) / old_range) * new_range + new_min

    return new_value    
        
    
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