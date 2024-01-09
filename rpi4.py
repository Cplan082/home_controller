# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:01:06 2024

@author: clive
"""

import paramiko
from paramiko.py3compat import u

class FileTransferServer(paramiko.ServerInterface):
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        return True

    def check_auth_password(self, username, password):
        return paramiko.AUTH_SUCCESSFUL

# Server configuration
host = '10.0.0.159'  # Replace with the actual IP address of the Raspberry Pi 4
port = 22  # Use port 22 or another port (e.g., 2222)

# Load your private key
private_key_path = '/home/clive/.ssh/id_rsa'  # Update this path
private_key = paramiko.RSAKey(filename=private_key_path)

# Create an SSH server
server = paramiko.Transport((host, port))
server.add_server_key(private_key)

# Start the server
try:
    server.start_server(server=FileTransferServer())
    print(f"Server listening on {host}:{port}")

    # Accept an incoming connection
    client, addr = server.accept()
    print(f"Accepted connection from {addr}")

    # Open a session for file transfer
    channel = client.accept(20)  # Open a "session" channel

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

finally:
    # Close the channel and the connection
    if channel:
        channel.close()
    client.close()
    server.close()




# import paramiko

# # Server configuration
# host = '10.0.0.159'  # Replace with the actual IP address of the Raspberry Pi 4
# port = 22

# # Create an SSH server
# server = paramiko.Transport((host, port))
# print("server created\n")

# # Load your private key (replace 'private_key_path' with the actual path)
# private_key_path = '/home/clive/.ssh/id_rsa'  # Update this path
# private_key = paramiko.RSAKey(filename=private_key_path)
# print("private key created\n")

# try:
#     # Start the server and wait for a connection
#     server.add_server_key(private_key)
#     server.start_server()

#     print(f"Server listening on {host}:{port}")

#     # Accept an incoming connection
#     client, addr = server.accept()
#     print(f"Accepted connection from {addr}")

#     # Open a session for file transfer
#     channel = client.open_channel('session')

#     # Specify the path where you want to save the received file
#     received_file_path = './data/test_received.csv'

#     # Receive the file and save it
#     with open(received_file_path, 'wb') as received_file:
#         file_data = b""
#         while True:
#             try:
#                 data = channel.recv(1024)
#                 if not data:
#                     break
#                 file_data += data
#             except EOFError:
#                 break  # Exit the loop when end-of-file is encountered

#         received_file.write(file_data)

#     print("File received successfully")

#     # Close the channel and the connection
#     channel.close()
#     client.close()
#     server.close()

# except Exception as e:
#     print(f"An error occurred: {e}")
#     raise