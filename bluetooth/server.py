import bluetooth

# Server configuration
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

server_socket.bind(("", port))
server_socket.listen(1)

print("Server waiting for connection...")

client_socket, client_info = server_socket.accept()
print(f"Accepted connection from {client_info}")

try:
    # Send a string to the client
    button_press = input("Press a button: ")
    print("\n")
    client_socket.send(button_press.encode('utf-8'))

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()
