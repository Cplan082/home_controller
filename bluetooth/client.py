import bluetooth
import pickle

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
        motor_speeds = pickle.loads(serialized_data)

        # Process the received motor speeds data
        print(f"Received Motor Speeds: {motor_speeds}")

except KeyboardInterrupt:
    print("Client terminated by user.")

finally:
    # Close the connection
    client_socket.close()