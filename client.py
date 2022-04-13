# We create a client that will connect to the server and send a message all the 1 minute

import socket
import time
import psutil

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port and the host on which you want to connect
host = "185.142.53.84"
port = 52365

connect = client_socket.connect((host, port))
print("Connected to the server")
while True:
    # Send a message with #01:01 and the ram usage
    cpu = f"#01:02,{int(psutil.cpu_percent(1))}".encode()
    ram = f"#01:01,{int(psutil.virtual_memory()[2])}".encode()
    client_socket.send(cpu)
    client_socket.send(ram)

    print("Message sent \nCPU:"+str(psutil.cpu_percent(4))+"%\nRAM:"+str(psutil.virtual_memory()[2])+"%")

    time.sleep(58)