# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:00:23 2024

@author: clive
"""
import paramiko

fname_csv = "test.csv"

# Server configuration
host = '0.0.0.0'  # Listen on all available interfaces
port = 12345

# Create an SSH server
server = paramiko.Transport((host, port))

# Load your private key (replace 'private_key_path' with the actual path)
private_key_path = '~/.ssh/id_rsa'
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

# Specify the path to the file you want to send
file_path = '/path/to/your/' + fname_csv

# Read the file and send its contents
with open(file_path, 'rb') as file:
    channel.sendall(file.read())

print("File sent successfully")

# Close the channel and the connection
channel.close()
client.close()
server.close()
