# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:00:23 2024

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
client.connect(username='clive', pkey=private_key)

# Open a session for file transfer
channel = client.open_channel('session')

# Specify the path to the file you want to send
file_path = './data/test.csv'

# Read the file and send its contents
with open(file_path, 'rb') as file:
    channel.sendall(file.read())

print("File sent successfully")

# Close the channel and the connection
channel.close()
client.close()
