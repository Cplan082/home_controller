# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:01:06 2024

@author: clive
"""

import paramiko

# Client configuration
host = '10.0.112'  # Replace with the actual IP address of the Raspberry Pi Zero W
port = 12345

# Create an SSH client
client = paramiko.Transport((host, port))

# Load your private key (replace 'private_key_path' with the actual path)
private_key_path = '~/.ssh/id_rsa'
private_key = paramiko.RSAKey(filename=private_key_path)

# Connect to the server
client.connect(username='your_username', pkey=private_key)

# Open a session for file transfer
channel = client.open_channel('session')

# Specify the path where you want to save the received file
received_file_path = './data/test.csv'

# Receive the file and save it
with open(received_file_path, 'wb') as received_file:
    received_file.write(channel.recv(1024))

print("File received successfully")

# Close the channel and the connection
channel.close()
client.close()
