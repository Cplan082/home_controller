import bluetooth

# Server configuration
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

server_socket.bind(("", port))
server_socket.listen(1)

print("Server waiting for connection...")

client_socket, client_info = server_socket.accept()
print(f"Accepted connection from {client_info}")

# Send a string to the client
message_to_send = "Hello, this is the server!"
client_socket.send(message_to_send.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()