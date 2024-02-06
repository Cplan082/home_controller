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
        
        
        
