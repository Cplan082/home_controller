# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:27:36 2024

@author: clive
"""

import pickle
import bluetooth

class server_BT:
    def __init__(self, port):
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

    def send_dict(self, dict_send):
        # Serialize the dictionary using pickle
        serialized_data = pickle.dumps(dict_send)
        
        # Send the serialized data to the connected client
        self.client_socket.send(serialized_data)
        
    def killInstance(self):
        # Close the client and server sockets when the instance is terminated
        self.client_socket.close()
        self.server_socket.close()


if __name__ == "__main__":
    import time
    import xbox_controller_interface as xci
    from mapping import dict_buttonMapping

    port = 1
    
    obj_xbc = xci.XboxControllerInterface(dict_buttonMapping)
    obj_server = server_BT(port)
    
    try:
        while True:
            obj_xbc.update_controllerStatus()
            obj_server.send_dict(obj_xbc.dict_controllerStatus)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Server/Controller terminated by user.")
    
    finally:
        obj_xbc.killInstance()
        obj_server.killInstance()
