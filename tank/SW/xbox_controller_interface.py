# -*- coding: utf-8 -*-
"""
Created on Fri Feb 2 23:56:01 2024

@author: clive
"""

import pygame
import sys
import os

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

class XboxControllerInterface:
    """
    XboxControllerInterface class for handling Xbox controller input using pygame.
    """

    def __init__(self, dict_buttonMapping):
        """
        Initializes the XboxControllerInterface class.

        Parameters:
            dict_buttonMapping (dict): Dictionary mapping button names to pygame constants.
        """
        # Initialize pygame
        self.pygame = pygame.init()

        # Create an instance for the Xbox controller
        self.controller = self.pygame.joystick.Joystick(0)

        # Initialize the Xbox controller
        self.controller.init()

        # Dictionary to map button names to their corresponding status
        self.dict_buttonMapping = dict_buttonMapping

        # Dictionary to store the current status of each mapped button
        self.dict_controllerStatus = {
            dict_buttonMapping["L_JOYSTICK_X"]: 0,
            dict_buttonMapping["L_JOYSTICK_Y"]: 0,
            dict_buttonMapping["R_JOYSTICK_X"]: 0,
            dict_buttonMapping["R_JOYSTICK_Y"]: 0,
            dict_buttonMapping["B_BUTTON"]: False,
            dict_buttonMapping["A_BUTTON"]: False,
            dict_buttonMapping["Y_BUTTON"]: False,
            dict_buttonMapping["X_BUTTON"]: False,
            dict_buttonMapping["START_BUTTON"]: False,
            dict_buttonMapping["BACK_BUTTON"]: False,
            dict_buttonMapping["L_TRIGGER"]: False,
            dict_buttonMapping["R_TRIGGER"]: False,
            dict_buttonMapping["L_BUMPER"]: False,
            dict_buttonMapping["R_BUMPER"]: False,
        }

    def update_controllerStatus(self):
        """
        Updates the status of the mapped buttons based on the events in the event queue.
        """
        # Iterate over all events in the event queue
        for event in self.pygame.event.get():
            # Check if the event is a joystick axis motion
            if event.type == self.pygame.JOYAXISMOTION:
                # Update the corresponding status in the dictionary based on the axis
                if event.axis == 0:
                    self.dict_controllerStatus[self.dict_buttonMapping["L_JOYSTICK_X"]] = event.value
                elif event.axis == 1:
                    self.dict_controllerStatus[self.dict_buttonMapping["L_JOYSTICK_Y"]] = event.value
                elif event.axis == 2:
                    self.dict_controllerStatus[self.dict_buttonMapping["R_JOYSTICK_X"]] = event.value
                elif event.axis == 3:
                    self.dict_controllerStatus[self.dict_buttonMapping["R_JOYSTICK_Y"]] = event.value

            elif event.type == self.pygame.JOYBUTTONDOWN:
                self.update_buttons(event.button, True)

            elif event.type == self.pygame.JOYBUTTONUP:
                self.update_buttons(event.button, False)

    def update_buttons(self, button, value):
        """
        Updates the status of the mapped buttons based on button press or release.

        Parameters:
            button (int): The button index.
            value (bool): The button status (pressed or released).
        """
        if button == 0:
            self.dict_controllerStatus[self.dict_buttonMapping["A_BUTTON"]] = value
        elif button == 1:
            self.dict_controllerStatus[self.dict_buttonMapping["B_BUTTON"]] = value
        elif button == 2:
            self.dict_controllerStatus[self.dict_buttonMapping["X_BUTTON"]] = value
        elif button == 3:
            self.dict_controllerStatus[self.dict_buttonMapping["Y_BUTTON"]] = value
        elif button == 4:
            self.dict_controllerStatus[self.dict_buttonMapping["L_BUMPER"]] = value
        elif button == 5:
            self.dict_controllerStatus[self.dict_buttonMapping["R_BUMPER"]] = value
        elif button == 6:
            self.dict_controllerStatus[self.dict_buttonMapping["BACK_BUTTON"]] = value
        elif button == 7:
            self.dict_controllerStatus[self.dict_buttonMapping["START_BUTTON"]] = value
        elif button == 8:
            self.dict_controllerStatus[self.dict_buttonMapping["L_TRIGGER"]] = value
        elif button == 9:
            self.dict_controllerStatus[self.dict_buttonMapping["R_TRIGGER"]] = value
            
            
    def killInstance(self):
        """
        Kills the Xbox controller and pygame instance.
        """
        # Kill the pygame instance
        self.pygame.quit()


if __name__ == "__main__":
    import time
    
    dict_buttonMapping ={"A_BUTTON": "A_BUTTON",
                         "B_BUTTON": "B_BUTTON",
                         "X_BUTTON": "X_BUTTON",
                         "Y_BUTTON": "Y_BUTTON",
                         "L_BUMPER": "L_BUMPER",
                         "R_BUMPER": "R_BUMPER",
                         "BACK_BUTTON": "BACK_BUTTON",
                         "START_BUTTON": "START_BUTTON",
                         "L_TRIGGER": "L_TRIGGER",
                         "R_TRIGGER": "R_TRIGGER",
                         "L_JOYSTICK_X": "L_JOYSTICK_X",
                         "L_JOYSTICK_Y": "L_JOYSTICK_Y",
                         "R_JOYSTICK_X": "R_JOYSTICK_X",
                         "R_JOYSTICK_Y": "R_JOYSTICK_Y",
                         }
    
    obj = XboxControllerInterface(dict_buttonMapping)
    
    try:
        while(True):
            obj.update_controllerStatus()
            print("\n===========================================\n")
            print(f"\tA_BUTTON     = {obj.dict_controllerStatus['A_BUTTON']}\n")
            print(f"\tB_BUTTON     = {obj.dict_controllerStatus['B_BUTTON']}\n")
            print(f"\tX_BUTTON     = {obj.dict_controllerStatus['X_BUTTON']}\n")
            print(f"\tY_BUTTON     = {obj.dict_controllerStatus['Y_BUTTON']}\n")
            print(f"\tL_BUMPER     = {obj.dict_controllerStatus['L_BUMPER']}\n")
            print(f"\tR_BUMPER     = {obj.dict_controllerStatus['R_BUMPER']}\n")
            print(f"\tBACK_BUTTON  = {obj.dict_controllerStatus['BACK_BUTTON']}\n")
            print(f"\tSTART_BUTTON = {obj.dict_controllerStatus['START_BUTTON']}\n")
            print(f"\tL_TRIGGER    = {obj.dict_controllerStatus['L_TRIGGER']}\n")
            print(f"\tR_TRIGGER    = {obj.dict_controllerStatus['R_TRIGGER']}\n")
            print(f"\tL_JOYSTICK_X = {obj.dict_controllerStatus['L_JOYSTICK_X']}\n")
            print(f"\tL_JOYSTICK_Y = {obj.dict_controllerStatus['L_JOYSTICK_Y']}\n")
            print(f"\tR_JOYSTICK_X = {obj.dict_controllerStatus['R_JOYSTICK_X']}\n")
            print(f"\tR_JOYSTICK_Y = {obj.dict_controllerStatus['R_JOYSTICK_Y']}\n")
            print("\n\n")
            time.sleep(0.1)  # Adjust delay as needed
            
    except KeyboardInterrupt:
        print("Controller terminated by user.")
    
    finally:
        obj.killInstance()