import bluetooth
import pickle
import pigpio


gpio_pin = 12
pwm_freq = int(1e6)

# Client configuration
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_address = "DC:A6:32:9C:1C:F5" # RPI4's bluetooth Address
port = 1 #Bluetooth port. Must match port used by server

pi = pigpio.pi()
if not pi.connected:
    exit()
    
pi.set_mode(gpio_pin, pigpio.OUTPUT)
client_socket.connect((server_address, port))

try:

    while True:
        # Receive motor speeds data from the server
        serialized_data = client_socket.recv(1024)
        if not serialized_data:
            break

        # Deserialize the received data
        data_joyStick = pickle.loads(serialized_data)
        x = data_joyStick['x_axis']
        y = data_joyStick['y_axis']
        mapped_y2pwm = data_joyStick['servoPwm_yAxis']
        pi.hardware_PWM(gpio_pin, pwm_freq, mapped_y2pwm)
        
        # Process the received motor speeds data
        print(f"Received Joystick Info: \n")
        print(f"\tX-Axis: {x}\n")
        print(f"\tY-Axis: {y}\n")
        print(f"\tPWM value: {mapped_y2pwm}\n\n")

except KeyboardInterrupt:
    print("Client terminated by user.")

finally:
    client_socket.close() # Close the connection
    pi.set_PWM_dutycycle(gpio_pin, 0)  # Stop PWM
    pi.stop()