# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:33:59 2024

@author: clive
"""

import time
import picamera

def main():
    # Create a PiCamera object
    with picamera.PiCamera() as camera:
        # Set the resolution as per your preference
        camera.resolution = (640, 480)
        # Camera warm-up time
        time.sleep(2)
        
        # Create a window for displaying the camera feed
        camera.start_preview()
        
        try:
            while True:
                # This loop will keep capturing and displaying frames until interrupted
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            # Close the preview window when the program is interrupted
            camera.stop_preview()

if __name__ == "__main__":
    main()