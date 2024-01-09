# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:01:06 2024

@author: clive
"""

import paramiko

# Server configuration
host = '10.0.0.159'  # Replace with the actual IP address of the Raspberry Pi 4
port = 22

# Create an SSH server
server = paramiko.Transport((host, port))

# Load your private key (replace 'private_key_path' with the actual path)
private_key_path = '/home/clive/.ssh/id_rsa'  # Update this path
private_key = paramiko.RSAKey(filename=private_key_path)

# Start the server and wait for a connection
server.add_server_key(private_key)
server.start_server()

print(f"Server listening on {host}:{port}")

# Accept an incoming connection
client, addr = server.accept()
print(f"Accepted connection from {addr}")

# Open a session for file transfer
channel = client.open_channel('session')

# Specify the path where you want to save the received file
received_file_path = './data/test_received.csv'

# Receive the file and save it
with open(received_file_path, 'wb') as received_file:
    file_data = b""
    while True:
        data = channel.recv(1024)
        if not data:
            break
        file_data += data
    received_file.write(file_data)

print("File received successfully")

# Close the channel and the connection
channel.close()
client.close()
server.close()
