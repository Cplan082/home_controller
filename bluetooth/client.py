import bluetooth

# Client configuration
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_address = "server_rpi_address"
port = 1

client_socket.connect((server_address, port))

# Receive the string from the server
received_data = client_socket.recv(1024).decode('utf-8')
print(f"Received: {received_data}")

# Close the connection
client_socket.close()