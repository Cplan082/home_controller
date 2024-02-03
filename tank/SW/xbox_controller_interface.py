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
        self.pygame.init()

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
