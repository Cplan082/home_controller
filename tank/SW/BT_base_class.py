# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:44:26 2024

@author: clive
"""

import pickle
import bluetooth

class BT_base:
    def __init__(self, port, server_address=None):
        self.get_client_socket(port, server_address)
        
    def get_client_socket(self, port, server_address):
        self.client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.client_socket.connect((server_address, port))
        
    def listen(self):
        serialized_data = self.client_socket.recv(self.rx_data_size_inBytes)
        
        if not serialized_data:
            return None
        
        return pickle.loads(serialized_data)
    
    def send_dict(self, dict_send):
        # Serialize the dictionary using pickle
        serialized_data = pickle.dumps(dict_send)
        
        # Send the serialized data to the connected client
        self.client_socket.send(serialized_data)
    
    def killInstance(self):
        self.client_socket.close() # Close the connection
        
        
        
class BT_client(BT_base):
    def __init__(self, port, server_address="DC:A6:32:9C:1C:F5"):
        super().__init__(port, server_address)
        
        

class BT_server(BT_base):
    def __init__(self, port):
        super().__init__(port)
        
    def get_client_socket(self, port):
        # Create a Bluetooth server socket using RFCOMM protocol
        self.server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        # Bind the server socket to the specified port and start listening
        self.server_socket.bind(("", port))
        self.server_socket.listen(1)
        
        # Print a message indicating that the server is waiting for a connection
        print("Server waiting for connection...")

        # Accept a connection from a client when available
        self.client_socket, self.client_info = self.server_socket.accept()
        print(f"Accepted connection from {self.client_info}")
        
    def killInstance(self):
        super().killInstance()
        self.server_socket.close() # Close the connection