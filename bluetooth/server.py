import pygame
import pickle
import bluetooth
import time

# Initialize pygame
pygame.init()

# Set up the Xbox controller
controller = pygame.joystick.Joystick(0)
controller.init()

# Define tank motor pins or functions
# Replace these with your actual motor control logic
def move_tank(x, y):
    # Adjust motor control logic based on xy coordinates
    # Example: Drive forward if y > 0, backward if y < 0
    # Turn left if x < 0, turn right if x > 0
    print(f"X: {x}, Y: {y}")

# Server configuration
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

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
                    x = event.value
                elif event.axis == 1:  # Left thumbstick y-axis
                    y = event.value

        move_tank(x, y)

        # Prepare motor speeds as a dictionary
        motor_speeds = {'left_motor': x, 'right_motor': y}

        # Serialize the data and send it to the client
        serialized_data = pickle.dumps(motor_speeds)
        client_socket.send(serialized_data)

        time.sleep(0.1)  # Adjust delay as needed

except KeyboardInterrupt:
    print("Script terminated by user.")

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
    pygame.quit()
