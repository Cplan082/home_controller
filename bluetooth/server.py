import pygame
import pickle
import bluetooth
import time
from ..common import common as cm

# Initialize pygame
pygame.init()

# Set up the Xbox controller
controller = pygame.joystick.Joystick(0)
controller.init()

port = 1 #Bluetooth port. Must match port used by client
pwm0_max_DC = 1000000 
pwm0_min_DC = 0

# Define tank motor pins or functions
# Replace these with your actual motor control logic
def displayTxData(x, y):
    # Adjust motor control logic based on xy coordinates
    # Example: Drive forward if y > 0, backward if y < 0
    # Turn left if x < 0, turn right if x > 0
    print(f"X: {x}, Y: {y}")
    
# def map_value(value, old_min, old_max, new_min, new_max):
#     """
#     Map a value from one range to another using linear mapping.

#     Parameters:
#     - value: The original value to be mapped.
#     - old_min: The minimum value of the original range.
#     - old_max: The maximum value of the original range.
#     - new_min: The minimum value of the desired range.
#     - new_max: The maximum value of the desired range.

#     Returns:
#     The mapped value in the new range.
#     """
#     old_range = old_max - old_min
#     new_range = new_max - new_min

#     # Perform linear mapping
#     new_value = ((value - old_min) / old_range) * new_range + new_min

#     return new_value


def saturate(value, minimum, maximum):
    """
    Saturate (clamp) a variable to a specified range.

    Parameters:
    - value: The variable to be saturated.
    - minimum: The minimum allowed value.
    - maximum: The maximum allowed value.

    Returns:
    The saturated value within the specified range.
    """
    return max(minimum, min(value, maximum))


# Server configuration
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

server_socket.bind(("", port))
server_socket.listen(1)

print("Server waiting for connection...")

client_socket, client_info = server_socket.accept()
print(f"Accepted connection from {client_info}")

try:
    x = 0
    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:  # Left thumbstick x-axis
                    x = saturate(event.value, -1, 1)
                elif event.axis == 1:  # Left thumbstick y-axis
                    y = saturate(event.value, -1, 1)

        displayTxData(x, y)
        mapped_y2pwm = round(cm.map_value(y, -1, 1, pwm0_min_DC, pwm0_max_DC))
        # Prepare motor speeds as a dictionary
        data_joyStick = {'x_axis': x, 'y_axis': y, 'servoPwm_yAxis': mapped_y2pwm}

        # Serialize the data and send it to the client
        serialized_data = pickle.dumps(data_joyStick)
        client_socket.send(serialized_data)

        time.sleep(0.1)  # Adjust delay as needed

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
    pygame.quit()
