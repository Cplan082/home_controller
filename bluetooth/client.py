import bluetooth
import pickle
import RPi.GPIO as GPIO

# Client configuration
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_address = "DC:A6:32:9C:1C:F5" # RPI4's bluetooth Address
port = 1

client_socket.connect((server_address, port))

try:
    while True:
        # Receive motor speeds data from the server
        serialized_data = client_socket.recv(1024)
        if not serialized_data:
            break

        # Deserialize the received data
        data_joyStick = pickle.loads(serialized_data)
        x = data_joyStick['x_axis']
        y = data_joyStick['y_axis']

        # Process the received motor speeds data
        print(f"Received Joystick Info: \n")
        print(f"\tX-Axis: {x}\n")
        print(f"\tY-Axis: {y}\n\n")

except KeyboardInterrupt:
    print("Client terminated by user.")

finally:
    # Close the connection
    client_socket.close()